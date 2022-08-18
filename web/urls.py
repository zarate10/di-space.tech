from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Inicio"),
    path("nosotros", views.nosotros, name="Nosotros"),
    path("celulares", views.celulares, name="Celulares"),
    path("computadoras", views.computadoras, name="Computadoras"),
    path("digital", views.digital, name="Digital"),
    path("redes", views.redes, name="Redes"),
    path("estado", views.estado, name="Estados")
]