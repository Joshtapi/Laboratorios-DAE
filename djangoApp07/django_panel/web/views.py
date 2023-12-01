from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import TblAlumno , TblProfesor
from .forms import AlumnoForm , ProfesorForm


class AlumnoView(View):
    def get(self, request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
            'alumnos': listaAlumnos,
            'formAlumno': formAlumno
        }
        return render(request, 'index.html', context)
    

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
        return redirect('web:index')


def eliminar_alumno(request, pk):
    listaAlumnos = TblAlumno.objects.get(pk=pk)
    listaAlumnos.delete()
    return redirect('web:index')

class ProfesorView(View):
    def get(self, request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
            'profesores': listaProfesores,
            'formProfesor': formProfesor
        }
        return render(request, 'profesores.html', context)

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
        return redirect('web:profesores')
    
def eliminar_profesor(request, pk):
    profesor = get_object_or_404(TblProfesor, pk=pk)
    profesor.delete()
    return redirect('web:profesores')

