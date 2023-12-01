from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


from blog.models import Categoria , Post
from .serializers import (CategoriaSerializer , PostSerializer)
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer