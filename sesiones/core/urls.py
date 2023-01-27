from django.urls import path
from .views import index, salir

urlpatterns = [
    path('', index, name='index'),
    path('salir', salir, name='salir'),
]