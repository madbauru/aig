from django.contrib import admin
from django.urls import path, include  # Adicione 'include' aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fileprocessor.urls')),  # Agora 'include' está definido
]
