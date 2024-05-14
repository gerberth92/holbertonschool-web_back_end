export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;
    }

    get code() {
        return this.code;
    }
    set code(code) {
        return this._code = code;
    }

    get name() {
        return this._name;
    }
    set name(name) {
        return this._name = name;
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}