#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);

  return (a + b);
}

const num1 = process.argv[2];
const num2 = process.argv[3];
const sum = add(num1, num2);

console.log(sum);
