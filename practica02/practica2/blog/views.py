from django.shortcuts import get_object_or_404, render
from .models import Post, Categoria
# Create your views here.
def index(request):
    post_list = Post.objects.order_by('titulo')[:6]
    categories_list = Categoria.objects.all()
    context = {
        'post_list' : post_list ,
        'categories_list': categories_list 
    }
    return render(request,'index.html',context)
def post(request, post_id):
    producto = get_object_or_404(Post, pk=post_id)

    return render(request,'post.html', {'producto': producto})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    post_list = categoria.post_set.all()
    categories_list = Categoria.objects.all()
    context = {
        'post_list' : post_list ,
        'categories_list': categories_list,
        'categoria':categoria
    }
    return render(request,'index.html',context)