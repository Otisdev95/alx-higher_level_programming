#!/usr/bin/node

exports.esrever = function (list) {
    const revList = [];
    for (let a = list.length - 1; a >= 0; a--) {
        revList.push(list[a]);
    }
    return revList;
};