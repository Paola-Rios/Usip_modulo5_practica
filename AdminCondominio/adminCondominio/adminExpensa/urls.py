from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views
#rREST API
# http://127.0.0.1:8000/adminExpensa/expensa/
router = DefaultRouter()
router.register(r"propietario", views.PropietarioViewSet)
router.register(r"departamento", views.DepartamentoViewSet)
router.register(r"expensaAgua", views.Expensa_AguaViewSet)
router.register(r"expensa", views.ExpensaViewSet)


urlpatterns= [
    path('contact/<str:name>', views.contact, name = 'contact'),
    path("", views.index, name = 'index'),
    path('propietarioV1/', views.propietario, name = 'propietario'),
    path('', include(router.urls))
]
