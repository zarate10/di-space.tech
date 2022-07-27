from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, "web/index.html", {
        "titulo": 'Inicio',
        "descripcion": 'Di Space Tech es una agencia de servicios informáticos. Brindamos reparación y mantenimiento de equipos (móviles y computadoras de escritorio y portátiles), además de la creación de sitios web.'
    })

def servicios(req):
    return render(req, "web/servicios.html", {
        "titulo": 'Servicios',
        "descripcion": '...'
    })

def nosotros(req):
    return render(req, "web/nosotros.html", {
        "titulo": 'Nosotros',
        "descripcion": '...'
    })

def contacto(req):
    return render(req, "web/contacto.html", {
        "titulo": 'Contacto',
        "descripcion": '...'
    })

def page_not_found_view(req, exception):
    return render(req, 'web/404.html', status=404)