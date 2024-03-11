#!/usr/bin/node

const count = process.argv[2];

if (count === undefined || isNaN(count)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < count; i++) {
    let row = '';
    for (let j = 0; j < count; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
