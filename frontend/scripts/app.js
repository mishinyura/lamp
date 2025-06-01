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



// const closeModal = () => {
//     openModalNow.classList.remove('show')
//     openModalNow.parentElement.classList.remove('show')
//     openModalNow = null
// }

// const openModal = (btn) => {
//     for (let modal of modals) {
//         if (modal.getAttribute('name') === btn.target.getAttribute('name')) {
//             modal.classList.add('show')
//             modal.parentElement.classList.add('show')
//             openModalNow = modal
//             modal.querySelector('.btn-close').addEventListener('click', closeModal)
//         }
//     }

// }

// const editMenu = () => {
//     menuContainer.classList.toggle('show')
// }





// const editViewAddBtn = (btn) => {
//     btn.target.classList.toggle('show')
//     let newBtn = btn.target.nextElementSibling
//     newBtn.classList.toggle('show')    
// }



// const editStateMainMenu = () => {
//     header.classList.toggle('header_close')
//     header.classList.toggle('header_open')
// }


// const indexInit = () => {
//     // addBtnCartPosition = document.querySelector('.cards__add');
//     burgerBtn = document.querySelector('.menu__burger');
//     menuContainer = document.querySelector('.menu__list');
//     addProductInCartBtns = document.querySelectorAll('.cards__add')

//     // addBtnCartPosition.addEventListener('click', upProduct)
//     burgerBtn.addEventListener('click', editMenu)

//     for (let btn of addProductInCartBtns) {
//         btn.addEventListener('click', editViewAddBtn)
//     }
// }


// const cartInit = () => {
//     addBtnCartPosition = document.querySelector('.product__up');
//     amountCartPosition = document.querySelector('.product__amount');
//     delBtnCartPosition = document.querySelector('.product__down');
//     productsInOrder = document.querySelectorAll('.product');
//     orderBtn = document.querySelector('.order__btn');

//     addBtnCartPosition.addEventListener('click', upProduct)
//     delBtnCartPosition.addEventListener('click', downProduct)

//     orderBtn.addEventListener('click', openModal)

//     for (let prod of productsInOrder) {
//         prod.addEventListener('click', delProduct)
//     }
// }

// const adminInit = () => {
//     burgerBtn = document.querySelector('.header__burger');
//     header = document.querySelector('.header');

//     burgerBtn.addEventListener('click', editStateMainMenu)
// }











// async function editAmountCountInCart(elem) {
//     let parent = elem.target.closest('li')
//     let counter = parent.querySelector('.cards__count')
//     let amount = counter.querySelector('.cards__amount')
//     let buyBtn = parent.querySelector('.cards__add')
//     let upBtn = counter.querySelector('.cards__up')
//     let downBtn = counter.querySelector('.cards__down')
//     let message = page.doc.querySelector('.notifications')

    
// };




// function changingViewBuyBtn(btn, counter){
//     let classBlock = counter.className.match(/.([a-zA-Z0-9]+)(?=__)/)[0]
//     let upBtn = counter.querySelector(`.${classBlock}__up`);
//     let downBtn = counter.querySelector(`.${classBlock}__down`);
//     btn.classList.toggle('show');
//     counter.classList.toggle('show');

//     if (btn.classList.contains('show')) {
//         btn.addEventListener('click', editAmountPositionInCard)
//         upBtn.removeEventListener('click', editAmountPositionInCard)
//         downBtn.removeEventListener('click', editAmountPositionInCard)
//     } else{
//         btn.removeEventListener('click', editAmountPositionInCard)
//         upBtn.addEventListener('click', editAmountPositionInCard)
//         downBtn.addEventListener('click', editAmountPositionInCard)
//     };
    
// };
    


// async function editAmountPositionInCard(elem) {
//     let parent = elem.target.closest('li')
//     let counter = parent.querySelector('.cards__count')
//     let amount = counter.querySelector('.cards__amount')
//     let buyBtn = parent.querySelector('.cards__add')
//     let data = {
//         article: String(parent.dataset.article),
//         amount: Number(amount.value)
//     };

//     if (amount.value == 0) {
//         amount.value = Number(amount.value) + 1
//         amount.setAttribute('value', amount.value)
//         changingViewBuyBtn(buyBtn, counter)
//         page.objects.cart.addProduct(data.article, data.amount)
//     } else {
//         if (elem.target.classList.contains('cards__down')) {
//             if (amount.value > 1) {
//                 amount.value = Number(amount.value) - 1
//                 amount.setAttribute('value', amount.value)
//             } else {
//                 amount.value = 0
//                 amount.setAttribute('value', amount.value)
//                 changingViewBuyBtn(buyBtn, counter)
//                 page.objects.cart.delProduct(data.article)
//             }
//         } else if(elem.target.classList.contains('cards__up')) {
            
//             let permission = await request(
//                 `http://localhost:8000/products/check`,
//                 'POST',
//                 data
//             );

//             if (permission) {
//                 amount.value = Number(amount.value) + 1
//                 amount.setAttribute('value', amount.value)
//                 page.objects.cart.addProduct(data.article, data.amount)
//             } else {
//                 let notification = new Notification('notifications')
//                 message = notification.messages.NOT_ENOUGH_PRODUCT
//                 notification.setMessage(message)
//                 notification.showMessage()
//             }
//         }
        
//     }
// }


// async function editAmountPositionInCart(elem) {
//     let parent = elem.target.closest('li')
//     let amount = parent.querySelector('.product__amount')
//     let data = {
//         article: String(parent.dataset.article),
//         amount: Number(amount.value)
//     };

//     if (elem.target.classList.contains('product__down')) {
//         page.objects.cart.delProduct(data.article)
//     } else {
//         let permission = await request(
//             `http://localhost:8000/products/check`,
//             'POST',
//             data
//         );

//         if (permission) {
//             page.objects.cart.addProduct(data.article, data.amount)
//         }
//     }
// }


function main() {
    startData = {
        'cart': cartInit,
        // 'admin': adminInit,
        'products': productsInit
    }

    startData[page.pageName]()
}




main()