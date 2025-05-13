const burgerBtn = document.querySelector('.header__burger'),
header = document.querySelector('.header');

const editStateMainMenu = () => {
    header.classList.toggle('header_close')
    header.classList.toggle('header_open')
}


burgerBtn.addEventListener('click', editStateMainMenu)