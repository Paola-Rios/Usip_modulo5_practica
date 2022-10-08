from django.shortcuts import render
from django.http import HttpResponse
from .models import Propietario
from .models import Departamento
from .models import Expensa_Agua
from .models import Expensa
from rest_framework import viewsets
from .serializers import PropietarioSerializer
from .serializers import DepartamentoSerializer
from .serializers import Expensa_AguaSerializer
from .serializers import ExpensaSerializer

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


class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = Propietario.objects.all()
    serializer_class = PropietarioSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class Expensa_AguaViewSet(viewsets.ModelViewSet):
    queryset = Expensa_Agua.objects.all()
    serializer_class = Expensa_AguaSerializer

class ExpensaViewSet(viewsets.ModelViewSet):
    queryset = Expensa.objects.all()
    serializer_class = ExpensaSerializer