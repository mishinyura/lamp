const pageName = document.querySelector('meta[name="pagename"]').content;

let burgerBtn, //Кнопка закрепить меню
header, //Основной header
addBtnCartPosition, //Кнопка увеличения объма товара в корзине
amountCartPosition, //Инпут количества товара в корзине
delBtnCartPosition, //Кнопка уменьшения объма товара в корзине
productsInOrder, //Товары в корзине
amountProducts,
amountProduct,
mainTotal,
productTotal;
let menuContainer;

let orderBtn;
let openModalNow;

let modals = document.querySelectorAll('.modals__modal');

function print(data) {
    console.log(data)
}

const upProduct = () => {
    amountProduct = Number(amountCartPosition.value);
    productTotal = Number()
    permission = true //Тут будет запрос к серверу на наличие такого количества
    if (permission && amountCartPosition.value < 99) {
        amountCartPosition.value = amountProduct + 1
    } else {
        amountCartPosition.value = 99
    }
}

const downProduct = () => {
    amountProduct = Number(amountCartPosition.value);
    if (amountProduct === 1) {
        amountCartPosition.value = 1
    } else {
        amountCartPosition.value = amountProduct - 1
    }
}

const delProduct = (elem) => {
    let product = elem.target
    product.parentNode.remove()
    console.dir(product)
}

const closeModal = () => {
    openModalNow.classList.remove('show')
    openModalNow.parentElement.classList.remove('show')
    openModalNow = null
}

const openModal = (btn) => {
    for (let modal of modals) {
        if (modal.getAttribute('name') === btn.target.getAttribute('name')) {
            modal.classList.add('show')
            modal.parentElement.classList.add('show')
            openModalNow = modal
            modal.querySelector('.btn-close').addEventListener('click', closeModal)
        }
    }

}

const editMenu = () => {
    menuContainer.classList.toggle('show')
}



const editStateMainMenu = () => {
    header.classList.toggle('header_close')
    header.classList.toggle('header_open')
}


const indexInit = () => {
    // addBtnCartPosition = document.querySelector('.cards__add');
    burgerBtn = document.querySelector('.menu__burger');
    menuContainer = document.querySelector('.menu__list');

    // addBtnCartPosition.addEventListener('click', upProduct)
    burgerBtn.addEventListener('click', editMenu)
}


const cartInit = () => {
    addBtnCartPosition = document.querySelector('.product__up');
    amountCartPosition = document.querySelector('.product__amount');
    delBtnCartPosition = document.querySelector('.product__down');
    productsInOrder = document.querySelectorAll('.product');
    orderBtn = document.querySelector('.order__btn');

    addBtnCartPosition.addEventListener('click', upProduct)
    delBtnCartPosition.addEventListener('click', downProduct)

    orderBtn.addEventListener('click', openModal)

    for (let prod of productsInOrder) {
        prod.addEventListener('click', delProduct)
    }
}

const adminInit = () => {
    burgerBtn = document.querySelector('.header__burger');
    header = document.querySelector('.header');

    burgerBtn.addEventListener('click', editStateMainMenu)
}


startData = {
    'cart': cartInit,
    'admin': adminInit,
    'index': indexInit
}

startData[pageName]()
