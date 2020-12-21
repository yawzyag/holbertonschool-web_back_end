import Currency from './3-currency';

function checkClass(classCheck, classOr) {
  return typeof classCheck === 'number' || classCheck instanceof classOr;
}

function checkNumber(numberCheck) {
  return typeof numberCheck === 'number' || numberCheck instanceof Number;
}

export default class Pricing {
  constructor(amount, currency) {
    if (checkNumber(amount)) {
      this._amount = amount;
    } else {
      throw TypeError('Amount must be a number');
    }
    if (checkClass(currency, Currency)) {
      this._currency = currency;
    } else {
      throw TypeError('Currency must be a Currency class');
    }
  }

  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (checkNumber(newAmount)) {
      this._amount = newAmount;
    } else {
      throw TypeError('Amount must be a number');
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (checkClass(newCurrency, Currency)) {
      this._currency = newCurrency;
    } else {
      throw TypeError('Currency must be a Currency class');
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    if (!checkNumber(amount)) {
      throw TypeError('Amount must be a number');
    }
    if (!checkNumber(conversionRate)) {
      throw TypeError('ConversionRate must be a number');
    }
    return amount * conversionRate;
  }
}
