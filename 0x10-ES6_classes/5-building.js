function checkNumber(numberCheck) {
  return typeof numberCheck === 'number' || numberCheck instanceof Number;
}

export default class Building {
  constructor(sqft) {
    if (checkNumber(sqft)) {
      this._sqft = sqft;
    } else {
      throw TypeError('Sqft must be a number');
    }
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (checkNumber(newSqft)) {
      this._sqft = newSqft;
    } else {
      throw TypeError('Sqft must be a number');
    }
  }
}
