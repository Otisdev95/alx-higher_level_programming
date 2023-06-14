#!/usr/bin/node

class Rectangle {
    constructor(width, height) {
        if (w > 0 && h > 0) {
            this.w = width;
            this.h = height;
        }  
    }

    print () {
        for (let a = 0; a < this.height; a++) {
            console.log('X'.repeat(this.width));
        }
    }
}

module.exports = Rectangle;