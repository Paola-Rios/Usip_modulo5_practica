from django.shortcuts import render
from django.http import HttpResponse
from .models import Propietario

# function view 
def index (request):
    return HttpResponse("hola mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de django")
def propietario(request):
#     post_carnet = request.POST.get('carnet')
#     post_nombre = request.POST.get('nombre')
#     post_apellido = request.POST.get('apellido')
#     post_correo = request.POST.get('correo')
#    # if post_carnet:
#         q= Propietario(carnet=post_carnet, nombre=post_nombre, apellido=post_apellido, correo=post_correo)
#         q.save()

    propietarios = Propietario.objects.all()
    return render(request,"propietario.html", {'propietarios': propietarios})