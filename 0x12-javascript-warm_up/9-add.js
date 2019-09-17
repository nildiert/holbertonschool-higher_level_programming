#!/usr/bin/node
/*
  js
*/
if (isNaN(parseInt(process.argv[2])) || isNaN(parseInt(process.argv[3]))) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
