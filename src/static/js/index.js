'use strict';


class Validator {
    validate(data) {
        for (let property in data) {
            if (data.hasOwnProperty(property)) {
                if (this.expression(data[property])) {
                    return false;
                }
            }
        }
        return true;
    }

    expression(property) {
        return /[~`!#$%@\^&*+=\-\[\]\\;,/{}|\\":<>\?]/.test(property) || /\d/.test(property);
    }
}


class AnswerElement {
    constructor() {
        this.instance = document.createElement('p');
        this.instance.className = 'answer';
        this.is_displayed = false;
    }

    setText(text) {
        this.instance.textContent = text;
    }

    display(node) {
        if (!this.is_displayed) {
            node.after(this.instance);
            this.is_displayed = true;
        }
    }
}


class FormElement {
    constructor(answerElement, validator) {
        this.instance = document.querySelector('.form');
        this.answerElement = answerElement;
        this.validator = validator;
    }

    submit(event) {
        event.preventDefault();
        let formData = this.getFormData();
        if (!this.validator.validate(formData)) {
            this.renderError("Ім'я чи прізвище не можуть мати числа або спеціальні символи!");
            return;
        }
        let jsonData = JSON.stringify(formData);
        let response = fetch(this.createRequest(jsonData))
            .then(response => response.json())
            .then(json => {
                this.renderAnswer(json, formData);
            });
    }

    getFormData() {
        let data = {};
        let formData = new FormData(this.instance);
        formData.forEach((value, key) => { data[key] = value });
        return data;
    }

    createRequest(body) {
        const url = window.location.href +'api/user_data';
        let headers = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf-8'
            },
            body: body
        };
        return new Request(url, headers)
    }

    renderAnswer(json, data) {
        if (json.status) {
            this.answerElement.setText(`Привіт, ${data.first_name} ${data.last_name}`);
            this.answerElement.display(this.instance);
        } else {
            this.answerElement.setText(`Вже зустрічались, ${data.first_name} ${data.last_name}`);
            this.answerElement.display(this.instance);
        }
    }

    renderError(error) {
        this.answerElement.setText(error);
        this.answerElement.display(this.instance);
    }
}


const validator = new Validator();
const answer = new AnswerElement();
const form = new FormElement(answer, validator);

form.instance.addEventListener('submit', (event) => { form.submit(event) });
