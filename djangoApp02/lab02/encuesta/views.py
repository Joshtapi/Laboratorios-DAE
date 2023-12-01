from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : "Formulario",
    }
    return render(request, 'encuesta/formulario.html' , context)

def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'nombre': request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def calculadora(request):
    context = {
        'titulo': 'Calculadora',
    }
    return render(request, 'encuesta/calculadora.html', context)

def resultado(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    operacion = request.POST['operacion']
    if operacion == 'suma':
        resultado = num1 + num2
        signo = '+'
    elif operacion == 'resta':
        resultado = num1 - num2
        signo = '-'
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        signo = 'x'
    else:
        resultado = None
        signo = None
    context = {
        'titulo': 'Resultado',
        'num1': num1,
        'num2': num2,
        'operacion': operacion,
        'signo': signo,
        'resultado': resultado,
    }
    return render(request, 'encuesta/resultado.html', context)

def cilindro(request):
    if request.method == 'POST':
        altura = float(request.POST.get('altura'))
        diametro = float(request.POST.get('diametro'))
        radio = diametro / 2
        volumen = 3.14 * radio * radio * altura
        context = {
            'volumen': volumen
        }
        return render(request, 'encuesta/resultado2.html', context)
    else:
        return render(request, 'encuesta/cilindro.html')