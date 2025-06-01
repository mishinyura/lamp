const SERVER = 'http://localhost:8000'

class Page{
    constructor() {
        this.objects = {}
        this.pageName = document.querySelector('meta[name="pagename"]').content;
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
        this.handleBuyBthClick = this.addProduct.bind(this)
        this.handleUpBthClick = this.addProduct.bind(this)
        this.handleDownBthClick = this.delProduct.bind(this)
        this.buyBtn.addEventListener('click', this.handleBuyBthClick)
    }

    create(){
        this.card = document.createElement('li')
        this.imageContainer = document.createElement('div')
        this.image = document.createElement('img')
        this.title = document.createElement('h3')
        this.price = document.createElement('span')
        this.counter = document.createElement('div')
        this.buyBtn = document.createElement('button')
        this.upBtn = document.createElement('button')
        this.downBtn = document.createElement('button')
        this.amount = document.createElement('input')

        this.card.classList.add(`${this.baseClass}__item`)
        this.imageContainer.classList.add(`${this.baseClass}__image`)
        this.title.classList.add(`${this.baseClass}__title`)
        this.price.classList.add(`${this.baseClass}__price`)
        this.counter.classList.add(`${this.baseClass}__count`)
        this.buyBtn.classList.add(`${this.baseClass}__add`)
        this.upBtn.classList.add(`${this.baseClass}__up`)
        this.downBtn.classList.add(`${this.baseClass}__down`)
        this.amount.classList.add(`${this.baseClass}__amount`)

        this.card.dataset.article = this.data.article
        this.image.setAttribute('src', `${SERVER}/static/${this.data.image_url}`)
        this.image.setAttribute('alt', this.data.title)
        this.title.innerHTML = this.data.title
        this.price.innerHTML = this.data.price
        this.buyBtn.classList.add(`${this.baseClass}__add`)
        this.buyBtn.classList.add('show')
        this.buyBtn.innerHTML = 'Купить'
        this.buyBtn.setAttribute('type', 'button')
        this.upBtn.setAttribute('type', 'button')
        this.downBtn.setAttribute('type', 'button')
        this.upBtn.innerHTML = '+'
        this.downBtn.innerHTML = '-'
        this.amount.setAttribute('value', '0')
        this.amount.setAttribute('name', 'product_amount')

        this.imageContainer.appendChild(this.image)

        this.counter.appendChild(this.downBtn)
        this.counter.appendChild(this.amount)
        this.counter.appendChild(this.upBtn)
        

        this.card.appendChild(this.imageContainer)
        this.card.appendChild(this.title)
        this.card.appendChild(this.price)
        this.card.appendChild(this.buyBtn)
        this.card.appendChild(this.counter)


        this.container.appendChild(this.card)

        return this.card
    }

    editViewBuyBtn(){
        this.buyBtn.classList.toggle('show');
        this.counter.classList.toggle('show');

        if (this.buyBtn.classList.contains('show')) {
            console.log('Сработало изменение кнопки с swow')
            this.buyBtn.addEventListener('click', this.handleBuyBthClick)
            this.upBtn.removeEventListener('click', this.handleUpBthClick)
            this.downBtn.removeEventListener('click', this.handleDownBthClick)
        } else{
            console.log('Сработало изменение кнопки без swow')
            this.buyBtn.removeEventListener('click', this.handleBuyBthClick)
            this.upBtn.addEventListener('click', this.handleUpBthClick)
            this.downBtn.addEventListener('click', this.handleDownBthClick)
        };
        
    };

    // editAmountInIcon(value) {
    //     let newValue = Number(this.cardCounter.innerHTML) + value;
    //     this.cardCounter.innerHTML = newValue;
    // }


    async addProduct() {
        // let item = this.products.find(obj => obj.hasOwnProperty(article));

        // if (item) {
        //     item[article] += amount
        // } else {
        //     this.products.push({[article]: amount})
        //     this.editAmountInIcon(1)
        // }
        // localStorage.setItem('cart', JSON.stringify(this.products))
        let newVal = Number(this.amount.value) + 1

        if (this.amount.value == 0) {
            this.amount.value = newVal
            this.editViewBuyBtn()
        } else {
            let data = {
                article: String(this.card.dataset.article),
                amount: newVal
            };

            let permission = await request(
                `http://localhost:8000/products/check`,
                'POST',
                data
            );

            if (permission) {
                this.amount.value = newVal
                // page.objects.cart.addProduct(data.article, data.amount)
            } else {
                let notification = new Notification('notifications')
                let message = notification.messages.NOT_ENOUGH_PRODUCT
                notification.setMessage(message)
                notification.showMessage()
            }
        }

        

        
    }

    delProduct() {
        // let index = this.products.findIndex(obj => obj.hasOwnProperty(article));

        // if (index !== -1) {
        //     this.products.splice(index, 1);
        //     this.editAmountInIcon(-1)
        // }
        // localStorage.setItem('cart', JSON.stringify(this.products))

        let newVal = Number(this.amount.value) - 1
        this.amount.value = newVal

        if (newVal < 1) {
            this.editViewBuyBtn()
        }
    }

    // async editAmountPositionInCard(elem) {
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
                
    //         } else if(elem.target.classList.contains('cards__up')) {
                
                
    //         }
            
    //     }
    // }
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