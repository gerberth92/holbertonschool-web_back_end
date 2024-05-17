export default class HolbertonCourse {
    constructor(name, length, students) {
        if (typeof name !== 'string') {
            throw TypeError('name debe de ser un string');
        }
        if (typeof length !== 'number') {
            throw TypeError('number debe de ser un numero');
        }
        if (!Array.isArray(students)) {
            throw TypeError('students debe de ser un array');
        }
        this._name = name;
        this._length = length;
        this._students = students
    }

    get name() {
        return this._name;
    }
    set name(name) {
        if (typeof name !== 'string') {
            throw TypeError('name debe de ser un string');
        }
        return this._name = name;
    }

    get length() {
        return this._length;
    }
    set length(length) {
        if (typeof length !== 'number') {
            throw TypeError('length debe de ser numero');
        }
        return this._length = length;
    }

    get students() {
        return this._students;
    }
    set students(students) {
        if (!Array.isArray(students)) {
            throw TypeError('students debe de ser un array');
        }
        return this._students = students;
    }
}
