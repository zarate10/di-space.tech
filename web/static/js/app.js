const $ = (element) => document.querySelector(element)

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

// bg 
let $$ = document.getElementById('canvas').getContext('2d')
let col = function (x, y, r, g, b) { 
    $$.fillStyle =`rgb(${r - 50}, ${g - 50}, ${b - 50})`
    $$.fillRect(x, y, 1, 1)
}

let R = function(x, y, t, colr) {
    return (Math.floor(colr - 20 * Math.cos((x * x - y * y) / 300 + t)))
}

let G = function(x, y, t, colg) {
    return (Math.floor(colg - 50 * Math.sin((x * x * Math.cos(t / 4) + y * y * Math.sin(t / 3)) / 300)))
}

let B = function(x, y, t, colb) {
    return (Math.floor(colb - 20 * Math.sin(5 * Math.sin(t / 9) + ((x - 100) * (x - 100) + (y - 100) * (y - 100)) / 1100)))
}

let t = 0

let run = function() {
    for (x = 0; x <= 35; x++){
        for (y = 0; y <= 35; y++){
     
            col(x, y, R(x, y, t, 255), G(x, y, t, 181), B(x, y, t, 106))
    
        }
    }
    t = t + 0.05
    window.requestAnimationFrame(run)
}

run()

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

function viewData(titulo, img, alt, descrip, time, price){ 
    if(titulo !== 'Otro'){
        const $windowService = $('.servicio-detalle')
        const $closeBtn = $('#cerrar')
    
        $('#sd-titulo').innerHTML = titulo
        $('#sd-img').setAttribute('src', img)
        $('#sd-img').setAttribute('alt', alt)
        $('#sd-descrip').innerHTML = descrip
        $('#sd-time').innerHTML = time
        $('#sd-price').innerHTML = price
    
        $windowService.style.marginRight = '0'
        console.log(titulo)
        $closeBtn.addEventListener('click', () => {
            $windowService.style.marginRight = '-100vw'
        })
    }
    
}