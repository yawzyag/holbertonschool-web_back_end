const checkString = (stringCheck) => typeof stringCheck === 'string' || stringCheck instanceof String;
export default class Currency {
  constructor(code, name) {
    if (checkString(name)) {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }
    if (checkString(code)) {
      this._code = code;
    } else {
      throw TypeError('Code must be a string');
    }
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (checkString(newName)) {
      this._name = newName;
    } else {
      throw TypeError('Name must be a string');
    }
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (checkString(newCode)) {
      this._code = newCode;
    } else {
      throw TypeError('Code must be a string');
    }
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
