export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  cast(type) {
    if (type === 'number') {
      return this._size;
    }
    if (type === 'string') {
      return this._location;
    }
    throw new TypeError('Invalid type for casting');
  }
}
