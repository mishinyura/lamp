const page = new Page

const productsInit = () => {
    page.addElement(new Cart, "cart")

    for (let btn of page.doc.querySelectorAll('.cards__add')) {
        btn.addEventListener('click', editAmountPositionInCard)
    }
}


const cartInit = () => {
    page.addElement(new Cart, "cart")

    for (let btn of page.doc.querySelectorAll('.product__down')) {
        btn.addEventListener('click', editAmountPositionInCart)
    }

    for (let btn of page.doc.querySelectorAll('.product__up')) {
        btn.addEventListener('click', editAmountPositionInCart)
    } 
}