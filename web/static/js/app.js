const $ = (element) => document.querySelector(element)

// inicio 
const $loader = $('.loader') 
if (window.data.title === 'Inicio'){

    document.body.style.overflowX = 'hidden'
    document.body.style.overflowY = 'hidden'
}

// Menu

let abierto = false;
const $botonToggle = $('.icon-menu')

const $contenedorMenu = $('.menu-options')
const $logo = $('#logo')

$botonToggle.addEventListener('click', () => {
    // console.log(abierto)
    abierto = !abierto

    if (abierto) {
        $contenedorMenu.style.display = 'flex'
        $contenedorMenu.style.transition = 'visibility 0s, opacity 1s'
        document.body.style.overflow = 'hidden';
        setTimeout(() => {            
            $contenedorMenu.style.visibility = 'visible'
            $contenedorMenu.style.opacity = '1'

            if (window.data.title !== 'Inicio'){
                $botonToggle.style.filter = 'invert(4000)'
                $logo.style.filter = 'invert(4000)'
            } 

        }, 50);
    } else {
        $botonToggle.removeAttribute('style')
        $logo.removeAttribute('style')
        $contenedorMenu.style.transition = 'visibility 1s, opacity 1s'
        $contenedorMenu.style.visibility = 'hidden'
        $contenedorMenu.style.opacity = '0'
        document.body.style.overflowY = 'scroll';
        setTimeout(() => {            
            $contenedorMenu.style.display = 'none'
        }, 700);
    }
    
})

// txt 

const txts = document.querySelector('.texts').children
const textInTimer = 3000
const textOutTimer = 2700

let i = 0;


function animateTxt() {

    for (let i = 0; i < txts.length; i++){ 
        txts[i].classList.remove("text-in", "text-out")
    }

    txts[i].classList.add("text-in")

    setTimeout(function(){
        txts[i].classList.add("text-out")
    }, textOutTimer)

    setTimeout(function(){
        if (i == txts.length - 1) {
            i = 0
        } else {
            i++; 
        }
        animateTxt()
    }, textInTimer)
}

// TO TOP 

const $btt = $('#btt')

$btt.addEventListener('click', () => {
    window.scrollTo(0,0)
})


document.addEventListener('DOMContentLoaded', () => {

    setTimeout(() => {
        $('#loader').style.animation = 'ready 1s'
        setTimeout(() => {
            $loader.style.animation = 'difuminado 0.5s'
        }, 300)
        setTimeout(() => {
            $loader.setAttribute('style', 'display: none;')
            document.body.style.overflowY = 'scroll'
            window.scrollTo(0,0)
        }, 600)
    }, 2000)

    animateTxt()
    window.onscroll = function() {
        // console.log(window.scrollY >= 1000)
        if (window.scrollY >= 300){
            document.querySelector('.back-to-top').style.marginBottom = "calc(100px + 1vh)"
        } else { 
            document.querySelector('.back-to-top').style.marginBottom = "-100vh"
        }
    }

    //reveal 
    window.sr = ScrollReveal(); 

    const toTop = { 
        duration: 2000,
        origin: 'top',
        distance: '-100px'
    }

    const toBottom = { 
        duration: 2000,
        origin: 'bottom',
        distance: '-100px'
    }

    const toRight = { 
        duration: 3000,
        origin: 'right',
        distance: '-100px'
    }

    sr.reveal('.box', toTop)
    sr.reveal('.title', toBottom)
    sr.reveal('.title_light', toBottom)
    sr.reveal('.descrip', toTop)
    sr.reveal('.toTop', toTop)

})

function viewData(titulo, img, alt, descrip, time, price, consulta){ 
    if(titulo !== 'Otro'){
        const $windowService = $('.servicio-detalle')
        const $closeBtn = $('#cerrar')
    
        $('#sd-wrapper').style.animation = 'aparece 1s ease-in'
        $('#sd-titulo').innerHTML = titulo
        $('#sd-img').setAttribute('src', img)
        $('#sd-img').setAttribute('alt', alt)
        $('#sd-descrip').innerHTML = descrip
        $('#sd-time').innerHTML = time
        $('#sd-price').innerHTML = price
        $('#sd-contacto').setAttribute('href', `https://wa.me/5492255629005?text=${consulta}`)
    
        setTimeout(() => { 
            $('#sd-wrapper').style.opacity = 1
            $windowService.style.marginRight = '0'
        }, 10)
    
        $closeBtn.addEventListener('click', () => {
            $('#sd-wrapper').style.animation = 'desaparece 1s ease-in'
            setTimeout(() => {
                $windowService.style.marginRight = '-100vw'
                $('#sd-wrapper').style.opacity = 0
            }, 100)
        })
    }
    
}