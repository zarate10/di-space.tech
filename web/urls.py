from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Inicio"),
    path("servicios", views.servicios, name="Servicios"),
    path("nosotros", views.nosotros, name="Nosotros"),
    path("contacto", views.contacto, name="Contacto")
]