SERVER = 'http://localhost:8000/'

class Page{
    constructor() {
        this.objects = {}
        this.pageName = document.querySelector('meta[name="pagename"]').content;
        this.updateDoc()
    }


    addElement(elem, name) {
        this.objects[name] = elem
        console.dir(this.objects)

    }

    updateDoc() {
        this.doc = document.querySelector('.body')
    }

    
}

class Notification{
    constructor(containerClassName) {
        this.messages = {
            DEFAULT: 'Что то пошло не так',
            NOT_ENOUGH_PRODUCT: 'Не хватает остатков на складе!',
            REPEAT_ACTION: 'Вы уже совершали это действие. Пожалуйста, подождите!'
        }

        this.notificationContainer = document.querySelector(`.${containerClassName}`)
        this.notificationDescr = this.notificationContainer.querySelector(`.${containerClassName}__descr`)
    }

    setMessage(message=this.messages.DEFAULT) {
        this.notificationDescr.innerHTML = message
    }

    showMessage(timer=5){
        this.notificationContainer.classList.add('show')
        setTimeout(() => {
            this.notificationContainer.classList.remove('show')
        }, timer * 1000);
    }
}


class Cart{
    constructor(){
        this.cartIconCounter = document.querySelector('.header__num');
        console.log('header num init')
        this.products = [];
    }


    editAmountInIcon(value) {
        let newValue = Number(this.cartIconCounter.innerHTML) + value;
        this.cartIconCounter.innerHTML = newValue;
    }


    addProduct(article, amount) {
        let item = this.products.find(obj => obj.hasOwnProperty(article));

        if (item) {
            item[article] += amount
        } else {
            this.products.push({[article]: amount})
            this.editAmountInIcon(1)
        }
    }

    delProduct(article) {
        let index = this.products.findIndex(obj => obj.hasOwnProperty(article));

        if (index !== -1) {
            this.products.splice(index, 1);
            this.editAmountInIcon(-1)
        }
    }

    sendCart() {
        let products = this.products
        this.products = []
        request(

        )
    }
}


class Card{
    constructor(containerClassName, productData){

        // console.log(this.products)

        // let product_id = products
        // let container = pa
        // this.cardCounter = document.querySelector('.header__num');
        // if (localStorage.getItem('cart')) {
        //     this.products = localStorage.getItem('cart')
        // } else {
        //     this.products = [];
        // }
        this.baseClass = containerClassName
        this.container = document.querySelector(`.${this.baseClass}`)
        this.data = productData
        this.create()
    }

    create(){
        let card = document.createElement('li')
        let imageContainer = document.createElement('div')
        let image = document.createElement('img')
        let title = document.createElement('h3')
        let price = document.createElement('span')
        let counter = document.createElement('div')
        let buyBtn = document.createElement('button')
        let upBtn = document.createElement('button')
        let downBtn = document.createElement('button')
        let amount = document.createElement('input')

        card.classList.add(`${this.baseClass}__item`)
        imageContainer.classList.add(`${this.baseClass}__image`)
        title.classList.add(`${this.baseClass}__title`)
        price.classList.add(`${this.baseClass}__price`)
        counter.classList.add(`${this.baseClass}__count`)
        buyBtn.classList.add(`${this.baseClass}__add`)
        upBtn.classList.add(`${this.baseClass}__up`)
        downBtn.classList.add(`${this.baseClass}__down`)
        amount.classList.add(`${this.baseClass}__amount`)

        card.dataset.article = this.data.article
        // image.setAttribute('src', `${SERVER}static/${data.image}`)
        image.setAttribute('alt', this.data.title)
        title.innerHTML = this.data.title
        price.innerHTML = this.data.price
        buyBtn.classList.add(`${this.baseClass}__add`)
        buyBtn.classList.add('show')
        buyBtn.innerHTML = 'Купить'
        // buyBtn.setAttribute('type', 'button')
        upBtn.setAttribute('type', 'button')
        downBtn.setAttribute('type', 'button')
        upBtn.innerHTML = '+'
        downBtn.innerHTML = '-'
        amount.setAttribute('value', '0')
        amount.setAttribute('name', 'product_amount')

        imageContainer.appendChild(image)

        counter.appendChild(downBtn)
        counter.appendChild(amount)
        counter.appendChild(upBtn)
        

        card.appendChild(imageContainer)
        card.appendChild(title)
        card.appendChild(price)
        card.appendChild(buyBtn)
        card.appendChild(counter)


        this.container.appendChild(card)

        return card
    }

    editAmountInIcon(value) {
        let newValue = Number(this.cardCounter.innerHTML) + value;
        this.cardCounter.innerHTML = newValue;
    }


    addProduct(article, amount) {
        let item = this.products.find(obj => obj.hasOwnProperty(article));

        if (item) {
            item[article] += amount
        } else {
            this.products.push({[article]: amount})
            this.editAmountInIcon(1)
        }
        localStorage.setItem('cart', JSON.stringify(this.products))
    }

    delProduct(article) {
        let index = this.products.findIndex(obj => obj.hasOwnProperty(article));

        if (index !== -1) {
            this.products.splice(index, 1);
            this.editAmountInIcon(-1)
        }
        localStorage.setItem('cart', JSON.stringify(this.products))
    }
}


class Menu{
    constructor(containerClassName) {
        this.nav = document.querySelector(`.${containerClassName}`)
        this.burger = this.nav.querySelector(`.${containerClassName}__burger`)
        this.list = this.nav.querySelector(`.${containerClassName}__list`)
    }
}

class TopMenu extends Menu {
    editState() {
        this.list.classList.toggle('show')
    }
}


// let cart = new Cart

// cart.addProduct('FF', 2)
// cart.addProduct('FF', 2)
// cart.addProduct('FD', 3)