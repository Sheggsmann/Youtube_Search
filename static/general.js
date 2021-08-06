// Nav Bar
const navToggle = document.querySelector('.nav-toggle')
const navBar = document.querySelector('.nav')

navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active')
    navBar.classList.toggle('show')
})