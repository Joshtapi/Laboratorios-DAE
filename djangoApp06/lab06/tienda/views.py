from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from .forms import ProductoForm

from .models import  Categoria, Producto

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    product_list = Producto.objects.order_by('nombre')[:6]
    context = {'product_list': product_list }
    context = {'categorias': categorias, 'product_list': product_list}
    return render(request, 'index.html', context)

def producto(request):
    producto = get_list_or_404(Producto, pk=producto)
    return render(request, 'producto.html', {'producto': producto})

def product_detail(request, pk):
    product = get_object_or_404(Producto, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = categoria.producto_set.all()
    context = {
        'categoria': categoria,
        'productos': productos
    }
    return render(request, 'productos_por_categoria.html', context)

def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('tienda:producto', producto_id=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto_editar.html', {'form': form})

def producto_editar(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('tienda:producto', producto_id=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_editar.html', {'form': form})