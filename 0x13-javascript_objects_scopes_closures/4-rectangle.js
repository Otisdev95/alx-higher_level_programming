#!/usr/bin/node

class Rectangle {
    constructor(width, height) {
        if (w > 0 && h > 0) {
            this.w = width;
            this.h = height;
        }  
    }

    print () {
        for (let a = 0; a < this.width; a++) {
            console.log('X'.repeat(this.height));
        }
    }

    rotate () {
        let temp = 0;
        temp = this.width;
        this.width = this.height;
        this.height = temp;
    }

    double () {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;