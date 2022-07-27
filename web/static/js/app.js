const $ = (element) => document.querySelector(element)

// CURSOR
const cursor = document.querySelector('.cursor');
const cursorBorder = document.querySelector('.cursor-out');

document.addEventListener('mousemove', (ev) => {
    cursor.style.left = ev.pageX + 'px';
    cursor.style.top = ev.pageY + 'px';
    cursorBorder.style.left = ev.pageX + 'px';
    cursorBorder.style.top = ev.pageY + 'px';
})

document.addEventListener('mouseover', (ev) => {
    if (ev.target.tagName == 'A'){
        cursorBorder.style.width = '70px'
        cursorBorder.style.height = '70px'
        cursorBorder.style.marginLeft = '-30px'
        cursorBorder.style.marginTop = '-30px'
    } else {
        cursorBorder.style.width = '40px'
        cursorBorder.style.height = '40px'
        cursorBorder.style.marginLeft = '-15px'
        cursorBorder.style.marginTop = '-15px'
    }

})

// Menu

let abierto = false;
let botonToggle = $('.icon-menu')

const $contenedorMenu = $('.menu-options')
const $logo = $('#logo')

botonToggle.addEventListener('click', () => {
    // console.log(abierto)
    abierto = !abierto

    if (abierto === true){
        botonToggle.setAttribute('style', 'filter: invert(4000)')
        $logo.setAttribute('style', 'filter: invert(4000)')
        $contenedorMenu.style.display = 'flex'
        $contenedorMenu.style.transition = 'visibility 0s, opacity 1s'
        document.body.style.overflow = 'hidden';
        setTimeout(() => {            
            $contenedorMenu.style.visibility = 'visible'
            $contenedorMenu.style.opacity = '1'
        }, 500);
    } else {
        botonToggle.removeAttribute('style')
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

// document.addEventListener('DOMContentLoaded', () => {
// })

