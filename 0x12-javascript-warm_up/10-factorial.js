#!/usr/bin/node
/*
  js
*/

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  const number = factorial(parseInt(process.argv[2]));
  console.log(number);
}
