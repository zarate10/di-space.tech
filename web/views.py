from django.shortcuts import render

# Create your views here.

cel_data = {
    "principal": 'Reparación y mantenimiento',
    "items": 
    [
        {
            "titulo": 'Cambio de módulo',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar"
        }, 
        {
            "titulo": 'Diagnóstico',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar"
        }, 
        {
            "titulo": 'Cambio flex',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar"
        }, 
        {
            "titulo": 'Otro'
        }
    ]
}

def index(req):
    return render(req, "web/index.html", {
        "titulo": 'Inicio',
        "descripcion": 'Di Space Tech es una agencia de servicios informáticos. Brindamos reparación y mantenimiento de equipos (móviles y computadoras de escritorio y portátiles), además de la creación de sitios web.'
    })

def celulares(req):
    return render(req, "web/celulares.html", {
        "titulo": 'Celulares',
        "descripcion": '...',
        "link_img": 'https://cyberdom.qodeinteractive.com/wp-content/uploads/2021/08/h8-img-03.png',
        "alt": 'Reparación de celulares DI SPACE TECH',
        "data": cel_data
    })

def computadoras(req):
    return render(req, "web/computadoras.html", {
        "titulo": 'Computadoras',
        "descripcion": '...'
    
    })

def digital(req):
    return render(req, "web/digital.html", {
        "titulo": 'Digital',
        "descripcion": '...'
    
    })

def nosotros(req):
    return render(req, "web/nosotros.html", {
        "titulo": 'Nosotros',
        "descripcion": '...'
    })

def redes(req):
    return render(req, "web/redes.html", {
        "titulo": 'Redes sociales',
        "descripcion": 'Di Space Tech es una agencia de servicios informáticos. Brindamos reparación y mantenimiento de equipos (móviles y computadoras de escritorio y portátiles), además de la creación de sitios web.'
    })


def page_not_found_view(req, exception):
    return render(req, 'web/404.html', {
        "titulo": '404',
        # "url": '{% url "Inicio" %}',
        "descripcion": '...'
    }, status = 404)