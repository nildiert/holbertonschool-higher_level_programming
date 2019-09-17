#!/usr/bin/node
/*
  js
*/
if (process.argv.length >= 3) {
  for (const i of process.argv.slice(2)) {
    console.log(i)
  }
} else {
  console.log('No argument')
}
