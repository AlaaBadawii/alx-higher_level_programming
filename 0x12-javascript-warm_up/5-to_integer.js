#!/usr/bin/node

const num = process.argv[2];

if (num === undefined) {
  console.log('Not a number');
} else if (!isNaN(num)) {
  console.log(`My number: ${parseInt(num)}`);
} else {
  console.log('Not a number');
}
