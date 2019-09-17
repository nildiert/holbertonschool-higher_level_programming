#!/usr/bin/node
/*
  js
*/

if (process.argv.length >= 3) {
    let size = process.argv[2]
    for (let i = 0; i < parseInt(size); i++) {
	console.log("X".repeat(size))
	}
} else {
    console.log("Missing size")
}
