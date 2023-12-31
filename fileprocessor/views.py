from django.shortcuts import render
from .models import Upload
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import textract
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        url = request.POST['url']
        upload = Upload(file=file, url=url)
        upload.save()
        print("Upload realizado com sucesso.")
        return HttpResponseRedirect('/progress')
    else:
        return render(request, 'index.html')

def progress(request):
    # Obtenha o último upload do usuário
    upload = Upload.objects.last()

    # Web scraping da URL
    if upload.url:
        print("Iniciando web scraping da URL...")
        try:
            response = requests.get(upload.url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remover cabeçalho, rodapé e barra lateral
            for tag in soup.find_all(['header', 'footer', 'sidebar', 'nav', 'aside']):
                tag.decompose()

            # Extrair todo o texto do corpo
            text = ' '.join(soup.body.stripped_strings)
            upload.results = text
            upload.save()
            print("Web scraping concluído com sucesso.")
        except Exception as e:
            print(f"Erro durante o web scraping: {e}")

    # Processar o arquivo
    if upload.file:
        print("Iniciando processamento do arquivo...")
        try:
            # Ler o arquivo
            file_content = textract.process(upload.file.path)
            print("Processamento do arquivo concluído com sucesso.")
        except Exception as e:
            print(f"Erro durante o processamento do arquivo: {e}")

    # Renderizar a página de progresso
    return render(request, 'progress.html')

def choose_product(request):
    if request.method == 'POST':
        # Obtenha o último upload do usuário
        upload = Upload.objects.last()

        # Atualize o campo do produto com a escolha do usuário
        upload.product = request.POST['product']
        upload.save()

        # Redirecione o usuário para a página de personalização
        return HttpResponseRedirect('/customize')
    else:
        return render(request, 'choose_product.html')

def customize(request):
    if request.method == 'POST':
        # Obtenha o último upload do usuário
        upload = Upload.objects.last()

        # Atualize o campo do título do e-book com o título enviado pelo usuário
        upload.ebook_title = request.POST.get('ebook_title', '')
        upload.blog_title = request.POST.get('blog_title', '')

        # Use GPT-3 para gerar o conteúdo do e-book ou post de blog
        try:
            print("Iniciando geração de conteúdo com GPT-3...")
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=upload.results,
                temperature=0.5,
                max_tokens=1000
            )
            upload.generated_content = response.choices[0].text.strip()
            upload.save()
            print("Geração de conteúdo com GPT-3 concluída com sucesso.")
        except Exception as e:
            print(f"Erro durante a geração de conteúdo com GPT-3: {e}")

        # Redirecione o usuário para a página de visualização
        return HttpResponseRedirect('/preview')
    else:
        return render(request, 'customize.html')

def preview(request):
    # Obtenha o último upload do usuário
    upload = Upload.objects.last()

    # Renderizar a página de visualização
    return render(request, 'preview.html', {'upload': upload})