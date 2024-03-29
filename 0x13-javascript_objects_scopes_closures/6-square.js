#!/usr/bin/node

const OtherSquare = require('./5-square');

class Square extends OtherSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;