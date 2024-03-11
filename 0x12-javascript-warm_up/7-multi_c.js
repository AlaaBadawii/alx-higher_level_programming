#!/usr/bin/node
const str = 'C is fun';
const count = process.argv[2];

for (let i = 0; i < count; i++) {
  console.log(str);
}
