class Page{
    constructor() {
        this.objects = {}
        this.pageName = document.querySelector('meta[name="pagename"]').content;
        this.doc = document.querySelector('.body')
    }


    addElement(elem, name) {
        this.objects[name] = elem
        console.dir(this.objects)

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
        console.log(`add product ${this.products}`)
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
}


class Card{
    constructor(cardClassName){
        let baseClass = cardClassName.match(/([a-zA-Z0-9]+)(?=__)/)[0]
        this.cardCounter = document.querySelector('.header__num');
        if (localStorage.getItem('cart')) {
            this.products = localStorage.getItem('cart')
        } else {
            this.products = [];
        }
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


// let cart = new Cart

// cart.addProduct('FF', 2)
// cart.addProduct('FF', 2)
// cart.addProduct('FD', 3)