from django.urls import path
from . import views

urlpatterns= [
    path('contact/<str:name>', views.contact, name = 'contact'),
    path ("", views.index, name = 'index'),
    path('propietario/', views.propietario, name = 'propietario')
]
