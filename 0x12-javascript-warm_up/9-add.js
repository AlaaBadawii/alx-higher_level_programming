#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (num1 === undefined || num2 === undefined) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
