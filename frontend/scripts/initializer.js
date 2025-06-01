const page = new Page()

async function productsInit() {
    page.addElement(new Cart, "cart")
    let menu = new TopMenu('menu')
    // let cards = new Card('cards')
    page.addElement(menu, "topmenu")
    page.addElement([], "cards")
    // page.updateDoc()
    // page.objects.card.addCardsInDom()

    let products = await request(
        `${SERVER}products`
    )

    for (let product of products) {
        let card = new Card('cards', product)
        page.objects.cards.push(card)
    }

    for (let btn of page.doc.querySelectorAll('.cards__add')) {
        btn.addEventListener('click', editAmountPositionInCard)
    }

    menu.burger.addEventListener('click', () => menu.editState())
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