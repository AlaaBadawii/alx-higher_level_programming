#!/usr/bin/node
let funCalled = 0;
exports.logMe = function (item) {
  console.log(`${funCalled}: ${item}`);
  funCalled++;
};
