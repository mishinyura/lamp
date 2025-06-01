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
        let sessionStore = localStorage.getItem('cart');
        this.products = sessionStore ? JSON.parse(sessionStore) : [];
        this.updateIcon();
    }


    updateIcon() {
        // Показываем сумму всех товаров в корзине
        let sum = this.products.reduce((acc, obj) => {
            const key = Object.keys(obj)[0];
            return acc + Number(obj[key]);
        }, 0);
        this.cartIconCounter.innerHTML = sum;
    }

    setLocalStore() {
        localStorage.setItem('cart', JSON.stringify(this.products));
    }

    async addProduct(article, amount) {
        let data = {
            article: article,
            amount: amount
        };
        let permission = await request(
            `http://localhost:8000/products/check`,
            'POST',
            data
        );

        if (permission) {
            let index = this.products.findIndex(obj => obj.hasOwnProperty(article));
            if (index !== -1) {
                this.products[index][article] = amount;
            } else {
                this.products.push({ [article]: amount });
            }
            this.setLocalStore();
            this.updateIcon();
            console.log(localStorage.getItem('cart'))
            return true;
        } else {
            let notification = new Notification('notifications');
            let message = notification.messages.NOT_ENOUGH_PRODUCT;
            notification.setMessage(message);
            notification.showMessage();
            console.log(localStorage.getItem('cart'))
            return false;
        }
    }

    delProduct(article) {
        let index = this.products.findIndex(obj => obj.hasOwnProperty(article));
        if (index !== -1) {
            this.products.splice(index, 1);
            localStorage.setItem('cart', JSON.stringify(this.products));
            this.updateIcon();
        }
        console.log(localStorage.getItem('cart'))
    }

    sendCart() {
        // Очищаем корзину и localStorage, если нужно
        let products = this.products;
        this.products = [];
        localStorage.removeItem('cart');
        this.updateIcon();
        // ...реализуй отправку корзины на сервер...
    }
}


class Card{
    constructor(containerClassName, productData){
        this.baseClass = containerClassName;
        this.container = document.querySelector(`.${this.baseClass}`);
        this.data = productData;
        this.create();

        this.handleBuyBtnClick = this.addProduct.bind(this);
        this.handleUpBtnClick = this.upProduct.bind(this);
        this.handleDownBtnClick = this.downProduct.bind(this);
        this.buyBtn.addEventListener('click', this.handleBuyBtnClick);
        this.upBtn.addEventListener('click', this.handleUpBtnClick);
        this.downBtn.addEventListener('click', this.handleDownBtnClick);
    }

    create(){
        this.card = document.createElement('li');
        this.imageContainer = document.createElement('div');
        this.image = document.createElement('img');
        this.title = document.createElement('h3');
        this.price = document.createElement('span');
        this.counter = document.createElement('div');
        this.buyBtn = document.createElement('button');
        this.upBtn = document.createElement('button');
        this.downBtn = document.createElement('button');
        this.amount = document.createElement('input');

        this.card.classList.add(`${this.baseClass}__item`);
        this.imageContainer.classList.add(`${this.baseClass}__image`);
        this.title.classList.add(`${this.baseClass}__title`);
        this.price.classList.add(`${this.baseClass}__price`);
        this.counter.classList.add(`${this.baseClass}__count`);
        this.buyBtn.classList.add(`${this.baseClass}__add`);
        this.upBtn.classList.add(`${this.baseClass}__up`);
        this.downBtn.classList.add(`${this.baseClass}__down`);
        this.amount.classList.add(`${this.baseClass}__amount`);

        this.card.dataset.article = this.data.article;
        this.image.setAttribute('src', `${SERVER}/static/${this.data.image_url}`);
        this.image.setAttribute('alt', this.data.title);
        this.title.innerHTML = this.data.title;
        this.price.innerHTML = this.data.price;
        this.buyBtn.classList.add('show');
        this.buyBtn.innerHTML = 'Купить';
        this.buyBtn.setAttribute('type', 'button');
        this.upBtn.setAttribute('type', 'button');
        this.downBtn.setAttribute('type', 'button');
        this.upBtn.innerHTML = '+';
        this.downBtn.innerHTML = '-';
        this.amount.setAttribute('type', 'number');
        this.amount.setAttribute('value', '0');
        this.amount.setAttribute('min', '0');
        this.amount.setAttribute('readonly', 'readonly');
        this.amount.setAttribute('name', 'product_amount');

        this.imageContainer.appendChild(this.image);

        this.counter.appendChild(this.downBtn);
        this.counter.appendChild(this.amount);
        this.counter.appendChild(this.upBtn);

        this.card.appendChild(this.imageContainer);
        this.card.appendChild(this.title);
        this.card.appendChild(this.price);
        this.card.appendChild(this.buyBtn);
        this.card.appendChild(this.counter);

        this.container.appendChild(this.card);

        // По умолчанию счетчик скрыт, кнопка купить видна
        this.counter.classList.remove('show');
        this.buyBtn.classList.add('show');

        return this.card;
    }

    editViewBuyBtn(){
        this.buyBtn.classList.toggle('show');
        this.counter.classList.toggle('show');
    };

    async addProduct() {
        this.amount.value = 1;
        this.editViewBuyBtn();
        page.objects.cart.addProduct(this.card.dataset.article, 1);
    }

    async upProduct() {
        let newVal = Number(this.amount.value) + 1;

        let permission = await page.objects.cart.addProduct(
            this.card.dataset.article, newVal
        );
        
        if (permission) {
            this.amount.value = newVal;
        };
    }

    downProduct() {
        let newVal = Number(this.amount.value) - 1;
        if (newVal > 0) {
            this.amount.value = newVal;
            page.objects.cart.addProduct(this.card.dataset.article, newVal);
        } else {
            this.amount.value = 0;
            page.objects.cart.delProduct(this.card.dataset.article);
            this.editViewBuyBtn();
        }
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