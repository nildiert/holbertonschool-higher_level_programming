#!/usr/bin/node
/*
  js
*/

function sortNumber (a, b) {
  return b - a;
}

if (process.argv.length < 4) {
  console.log(0);
} else {
  const myArray = [];
  const sliceArray = process.argv.slice(2);
  for (const i of sliceArray) {
    myArray.push(Number(i));
  }

  myArray.sort(sortNumber);
  console.log(myArray[1]);
}
