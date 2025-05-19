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

let addProductInCartBtns;

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





const editViewAddBtn = (btn) => {
    btn.target.classList.toggle('show')
    let newBtn = btn.target.nextElementSibling
    newBtn.classList.toggle('show')    
}



const editStateMainMenu = () => {
    header.classList.toggle('header_close')
    header.classList.toggle('header_open')
}


const indexInit = () => {
    // addBtnCartPosition = document.querySelector('.cards__add');
    burgerBtn = document.querySelector('.menu__burger');
    menuContainer = document.querySelector('.menu__list');
    addProductInCartBtns = document.querySelectorAll('.cards__add')

    // addBtnCartPosition.addEventListener('click', upProduct)
    burgerBtn.addEventListener('click', editMenu)

    for (let btn of addProductInCartBtns) {
        btn.addEventListener('click', editViewAddBtn)
    }
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

// startData[pageName]()


class Page{
    constructor(elements) {
        this.objects = elements
        // console.log(elements)
        // for (let elem in elements) {
        //     console.log(elements[elem])
        // }
        
        this.doc = document.querySelector('.body')
    }

    
}

const page = new Page({
    data: 'ok'
});


async function editAmountPositionInCard(elem) {
    let parent = elem.target.closest('li')
    let counter = parent.querySelector('.cards__count')
    let amount = counter.querySelector('.cards__amount')
    let buyBtn = parent.querySelector('.cards__add')
    let upBtn = counter.querySelector('.cards__up')
    let downBtn = counter.querySelector('.cards__down')
    let message = page.doc.querySelector('.notifications')

    if (amount.value == 0) {
        amount.value = Number(amount.value) + 1
        amount.setAttribute('value', amount.value)
        console.log(amount.value)

        buyBtn.classList.remove('show')
        counter.classList.add('show')
        upBtn.addEventListener('click', editAmountPositionInCard)
        downBtn.addEventListener('click', editAmountPositionInCard)

    } else {
        if (elem.target.classList.contains('cards__down')) {
            if (amount.value > 1) {
                amount.value = Number(amount.value) - 1
                amount.setAttribute('value', amount.value)
            } else {
                buyBtn.classList.add('show')
                counter.classList.remove('show')

                amount.value = 0
                amount.setAttribute('value', amount.value)

                upBtn.removeEventListener('click', editAmountPositionInCard)
                downBtn.removeEventListener('click', editAmountPositionInCard)
            }
        } else if(elem.target.classList.contains('cards__up')) {
            let permission = await request(
                `http://localhost:8000/products/check`,
                'POST',
                {
                    article: parent.dataset.article,
                    count: amount.value
                }
            )

            if (permission) {
                amount.value = Number(amount.value) + 1
                amount.setAttribute('value', amount.value)
            } else {
                message.classList.add('show')
                setTimeout(() => {
                    message.classList.remove('show')
                }, 5000);
                
            }
        }
        
    }
}


async function main() {
    // console.log(page.doc.querySelectorAll('.cards__add'))

    for (let btn of page.doc.querySelectorAll('.cards__add')) {
        btn.addEventListener('click', editAmountPositionInCard)
    }
}

main()