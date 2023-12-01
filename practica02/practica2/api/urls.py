from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', views.PostViewSet,basename="post")
router.register(r'categoria', views.CategoriaViewSet,basename="categoria")

urlpatterns = [
    path('admin/',include(router.urls))
]