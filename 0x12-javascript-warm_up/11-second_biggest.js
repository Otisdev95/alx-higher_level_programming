#!/usr/bin/node

const arr = process.argv.slice(2);
function second (array) {
    if (array.length < 2) {
        return (0);
    } else {
        array.sort((x, y) => x - y);
        array.pop();
        return (array.pop());
    }
}
console.log(second(arr));