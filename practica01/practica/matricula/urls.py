from django.urls import path
from . import views

app_name = 'matricula'

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('posiciones/', views.posiciones, name='posiciones'),
]