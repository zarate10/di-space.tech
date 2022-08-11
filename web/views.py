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
            "descrip": "Si notas que tu dispositivo ya no es tan rápido como antes, ésta es tu sección. Lograremos que tu dispositivo vuelva a su velocidad usual mediante limpiezas técnicas de software. ",
            "tiempo": "2 Días",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de celulares: "
        }, 
        {
            "titulo": 'Reparación general',
            "img": "https://i.imgur.com/vT7raCy.png",
            "alt": "Servicio técnico celular",
            "descrip": "Repararemos tu dispositivo ante cualquier avería o falla y te daremos a conocer el error que posee",
            "tiempo": "1 Día",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de celulares: "
        }, 
        {
            "titulo": 'Reemplazo de componentes',
            "img": "https://i.imgur.com/fZEzJ4Y.png",
            "alt": "Servicio técnico celular",
            "descrip": "Cambiaremos cualquier componente que falle en tu dispositivo. <br> Desde el modulo de tu celular, hasta el pin de carga. ",
            "tiempo": "2 Días + Envío ",
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
            "img": "https://i.imgur.com/RndV2Hp.png",
            "alt": "Servicio técnico pc",
            "descrip": "Si notas que tu Computadora necesita una limpieza, ya sea física o virtual, esta es tu sección. Lograremos dar un aspecto reluciente y agilizar el funcionamiento de tu dispositivo mediante las mejores herramientas.",
            "tiempo": "2 Días",
            "precio": "500 Ars",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Optimización del sistema',
            "img": "https://i.imgur.com/lyifBS3.png",
            "alt": "Servicio técnico pc",
            "descrip": "¿Notas tu sistema operativo lento y torpe? No te preocupes, mediante un minucioso trabajo, lograremos que tu SO (Sistema operativo) funcione al 100%.",
            "tiempo": "1 Día  ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Reemplazo de componentes',
            "img": "https://i.imgur.com/ciqYRo3.png",
            "alt": "Servicio técnico pc",
            "descrip": "¿Te gustaría que tu computadora de escritorio funcione mucho mejor que como funciona en este momento? No deseches tu equipo, ya que mediante un reemplazo por componentes de                 un mejor nivel tu mejor amigo con teclas logrará superarse.",
            "tiempo": "2 Días + Envío ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al servicio técnico de pc: "
        }, 
        {
            "titulo": 'Armado y presupuesto',
            "img": "https://i.imgur.com/qyWqYpy.png",
            "alt": "Servicio técnico pc",
            "descrip": "¿Te gustaría empezar en el mundo del gaming,? o tal vez necesitas una computadora para tu trabajo. No busques más, nosotros te proporcionaremos un presupuesto según tus                                  necesidades y si es el caso llevaremos ese presupuesto a la realidad y te ensamblaremos tu computadora personal. ",
            "tiempo": "1 Día + Envío componentes ",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al armado y presupuesto de pc: "
        },
        {
            "titulo": 'Instalación de S.O y apps',
            "img": "https://i.imgur.com/RndV2Hp.png",
            "alt": "Servicio técnico pc",
            "descrip": "Si usted compró una computadora y esta no posee un sistema operativo (Como puede ser Windows), no se preocupe nosotros nos ofrecemos para solucionar ese problema. <br>                            También usted puede requerir programas como Microsoft Word y Microsoft Excel, entre otros, los cuales nosotros brindamos.",
            "tiempo": "2 Días",
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
            "img": "https://www.technipages.com/wp-content/uploads/2020/09/java-and-javascript-header.png",
            "alt": "SaaS - Di Space Tech",
            "descrip": "¿Por qué tener un sitio web?<br><br><strong>Dos aspectos vitales:</strong> El primer aspecto: un espacio donde sólo está tu negocio. En otras plataformas, la atención del potencial cliente puede verse afectada por ofertas de otro negocio, mientras que en un sitio web propio, podrás transmitir todo lo tu negocio significa y representa, sin correr ese riesgo. <br><br>Por otro lado, desde un aspecto más técnico, podemos trabajar para que tu sitio web se posicione entre los primeros, sino el primero, en el motor de búsqueda de Google. Haciéndote visible (mayor publicidad) para todo aquel que esté buscando un negocio con tus características en el gigante de internet.",
            "tiempo": "Mínimo dos semanas",
            "precio": "Consultar",
            "consulta": "Hola, quiero consultar respecto al desarrollo web"
        }, 
        {
            "titulo": 'Diseño de marca gráfica',
            "img": "https://www.brandesign.es/wp-content/uploads/2020/08/que-es-el-branding-brandesign.jpg",
            "alt": "SaaS - Di Space Tech",
            "descrip": "Próxoimamente",
            "tiempo": "SIN DISPONIBILIDAD",
            "precio": "SIN DISPONIBILIDAD",
            "consulta": "Hola, quiero consultar respecto al desarrollo web"
        }, 
        {
            "titulo": 'Community Management',
            "img": "https://josefacchin.com/wp-content/uploads/2020/07/community-manager-que-es.png",
            "alt": "SaaS - Di Space Tech",
            "descrip": "Próximamente",
            "tiempo": "SIN DISPONIBILIDAD",
            "precio": "SIN DISPONIBILIDAD",
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