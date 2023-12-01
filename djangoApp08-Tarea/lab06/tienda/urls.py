from django import views
from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:producto_id>/', views.producto, name='producto'),
    path('producto/<int:pk>/', views.product_detail, name='product_detail'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:producto_id>/editar/', views.producto_editar, name='producto_editar'),
]