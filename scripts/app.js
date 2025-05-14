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

const editStateMainMenu = () => {
    header.classList.toggle('header_close')
    header.classList.toggle('header_open')
}


const indexInit = () => {
    addBtnCartPosition = document.querySelector('.cards__add');

    addBtnCartPosition.addEventListener('click', upProduct)
}


const cartInit = () => {
    addBtnCartPosition = document.querySelector('.product__up');
    amountCartPosition = document.querySelector('.product__amount');
    delBtnCartPosition = document.querySelector('.product__down');
    productsInOrder = document.querySelectorAll('.product');

    addBtnCartPosition.addEventListener('click', upProduct)
    delBtnCartPosition.addEventListener('click', downProduct)

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
    'admin': adminInit
}

startData[pageName]()
