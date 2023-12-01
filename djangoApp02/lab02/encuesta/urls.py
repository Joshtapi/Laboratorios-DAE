from django.urls import path

from . import  views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('calculadora', views.calculadora, name='calculadora'),
    path('cilindro', views.cilindro, name='cilindro'),
    path('resultado', views.resultado, name='resultado'),

]
