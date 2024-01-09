#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  show () {
    let i = 0;
    while (i < this.height) {
      let s = '';
      let j = 0;
      while (j < this.width) {
        s += 'X';
        j++;
      }
      console.log(s);
      i++;
    }
  }
}

module.exports = Rectangle;
