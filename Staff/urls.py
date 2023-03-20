from django.urls import path
from Staff.views import *


urlpatterns = [

    path('', index, name="index"),
    path('cursos/', cursos, name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    
]
