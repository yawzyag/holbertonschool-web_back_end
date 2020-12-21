const checkArr = (x) => x.every((i) => typeof i === 'string');
const checkString = (stringCheck) => typeof stringCheck === 'string' || stringCheck instanceof String;
const checkNumber = (numberCheck) => typeof numberCheck === 'number' || numberCheck instanceof Number;

export default class HolbertonCourse {
  constructor(name, length, students) {
    if (checkString(name)) {
      this._name = name;
    } else {
      throw TypeError('Name must be a string');
    }

    if (checkNumber(length)) {
      this._length = length;
    } else {
      throw TypeError('Length must be a number');
    }

    if (checkArr(students)) {
      this._students = students;
    } else {
      throw TypeError('students must be an array of strings');
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

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (checkNumber(newLength)) {
      this._length = newLength;
    } else {
      throw TypeError('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (checkArr(newStudents)) {
      this._students = newStudents;
    } else {
      throw TypeError('students must be an array of strings');
    }
  }
}
