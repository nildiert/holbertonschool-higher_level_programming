#!/usr/bin/node
/*
  js
*/
if (process.argv.length >= 3) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
