from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'Staff/index.html')

def cursos(request):
    return render(request, 'Staff/cursos.html')

def estudiantes(request):
    return render(request, 'Staff/estudiantes.html')

def profesores(request):
    return render(request, 'Staff/profesores.html')

def entregables(request):
    return render(request, 'Staff/entregables.html')