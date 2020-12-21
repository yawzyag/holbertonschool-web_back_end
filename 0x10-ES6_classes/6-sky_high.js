import Building from './5-building';

function checkNumber(numberCheck) {
  return typeof numberCheck === 'number' || numberCheck instanceof Number;
}

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    if (checkNumber(floors)) {
      this._floors = floors;
    } else {
      throw TypeError('Floors must be a number');
    }
  }

  get floors() {
    return this._floors;
  }

  set floors(newFloors) {
    if (checkNumber(newFloors)) {
      this._floors = newFloors;
    } else {
      throw TypeError('Floors must be a number');
    }
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
