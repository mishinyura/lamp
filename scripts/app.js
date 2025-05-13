const pageName = document.querySelector('meta[name="pagename"]').content;

let burgerBtn,
header,
addBtnCartPosition,
amountCartPosition,
delBtnCartPosition,
amountProducts,
amountProduct,
mainTotal,
productTotal;

const upProduct = () => {
    amountProduct = Number(amountCartPosition.value);
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

const delProduct = () => {
    
}

const editStateMainMenu = () => {
    header.classList.toggle('header_close')
    header.classList.toggle('header_open')
}


const cartInit = () => {
    addBtnCartPosition = document.querySelector('.product__up');
    amountCartPosition = document.querySelector('.product__amount');
    delBtnCartPosition = document.querySelector('.product__down');

    
    productTotal = Number()


    addBtnCartPosition.addEventListener('click', upProduct)
    delBtnCartPosition.addEventListener('click', downProduct)
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
