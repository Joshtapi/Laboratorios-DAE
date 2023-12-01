from django.urls import path, include 
from rest_framework import routers
from .views import *

#librerias para visualizar las imagenes
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register('vehiculos', TblVehiculoViewSet)
router.register('documentos', TblVehiculoDocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/<str:search>', SearchVehiculoView.as_view()),

]