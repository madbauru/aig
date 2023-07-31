from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('progress', views.progress, name='progress'),
    path('choose_product', views.choose_product, name='choose_product'),
    path('customize', views.customize, name='customize'),
]