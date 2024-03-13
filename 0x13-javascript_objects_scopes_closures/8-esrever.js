#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const mid = Math.floor(len / 2);
  for (let i = 0; i < mid; i++, len--) {
    const temp = list[i];
    list[i] = list[len - 1];
    list[len - 1] = temp;
  }

  return list;
};
