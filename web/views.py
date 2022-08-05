from django.shortcuts import render

# Create your views here.

cel_data = {
    "principal": 'Reparación y mantenimiento',
    "items": 
    [
        {
            "titulo": 'Mantenimiento',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de celulares: "
        }, 
        {
            "titulo": 'Reparación general',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de celulares: "
        }, 
        {
            "titulo": 'Reemplazo de componentes',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico celular",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de celulares: "
        }
    ]
}

pc_data = {
    "principal": 'Reparación y mantenimiento',
    "items": 
    [
        {
            "titulo": 'Limpieza y mantenimiento',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico pc",
            "descrip": "Seleccionamos los mejores componentes en base a tus preferencias.",
            "tiempo": "Sin demora",
            "precio": "Gratis",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Optimización del sistema',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico pc",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Reemplazo de componentes',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico pc",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Armado y presupuesto',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico pc",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        },
        {
            "titulo": 'Instalación de S.O y apps',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "Servicio técnico pc",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }
    ]
}

digital_data = {
    "principal": 'Potenciamos tu negocio',
    "items": 
    [
        {
            "titulo": 'Desarrollo de sitio web',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "SaaS - Di Space Tech",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al desarrollo web"
        }, 
        {
            "titulo": 'Diseño de marca gráfica',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "SaaS - Di Space Tech",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al desarrollo web"
        }, 
        {
            "titulo": 'Community Management',
            "img": "https://fixexperts.in/wp-content/uploads/2021/06/fix.jpeg",
            "alt": "SaaS - Di Space Tech",
            "descrip": "Loreminsun",
            "tiempo": "2 D  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al desarrollo web"
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
        "link_img": 'https://i.imgur.com/AnSh0K0.png',
        "alt": 'Reparación y mantenimiento de celulares DI SPACE TECH',
        "data": cel_data

    })

def computadoras(req):
    return render(req, "web/computadoras.html", {
        "titulo": 'Computadoras',
        "descripcion": '...',
        "link_img": 'https://static.wixstatic.com/media/95a5b7_68435ed45cee44b7b9d5cb7eb3ae9959~mv2.png/v1/crop/x_207,y_0,w_1670,h_2084/fill/w_640,h_738,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/GABINETES_SWORD%20PX.png',
        "alt": 'Reparación y mantenimiento de computadoras DI SPACE TECH',
        "data": pc_data
  
    })

def digital(req):
    return render(req, "web/digital.html", {
        "titulo": 'Digital',
        "descripcion": '...',
        "link_img": 'https://i.imgur.com/GMcsOGc.png',
        "alt": 'Servicios digitales DI SPACE TECH',
        "data": digital_data

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