from django.shortcuts import render
from .models import Upload
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        url = request.POST['url']
        upload = Upload(file=file, url=url)
        upload.save()
        return HttpResponseRedirect('/progress')
    else:
        return render(request, 'index.html')

def progress(request):
    # Aqui você pode adicionar o código para processar o arquivo e a URL
    # Por enquanto, vamos apenas renderizar o template 'progress.html'
    return render(request, 'progress.html')
