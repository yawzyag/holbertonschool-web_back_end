export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    const orig = this;
    return Object.assign(Object.create(Object.getPrototypeOf(orig)), {
      _brand: undefined,
      _motor: undefined,
      _color: undefined,
    });
  }
}
