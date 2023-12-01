from django.shortcuts import render
from .models import Pregunta, Opcion

# Create your views here.
# Create your views here.
def index(request):
    lista_preguntas = Pregunta.objects.all()
    context= {
        'preguntas':lista_preguntas
    }
    return render(request, 'index.html', context)

def registro(request):
    data_nombre = request.POST['nombre']
    data_email = request.POST['email']

    objAlumno = Alumno.objects.create(
        nombre = data_nombre,
        email = data_email
    )

    objNota = Nota(nota=data_nota, alumno=objAlumno)
    objNota.save()

    context = {
        'notas':Nota.objects.all()
    }

    return render(request, 'posiciones.html', context)
