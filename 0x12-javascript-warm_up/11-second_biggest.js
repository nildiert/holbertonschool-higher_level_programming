#!/usr/bin/node
/*
  js
*/

function sortNumber(a, b) {
    return b - a
}

if (process.argv.length === 2) {
    console.log(0)
} else {
    my_array = []
    slice_array = process.argv.slice(2)
    for (i of slice_array) {
	my_array.push(Number(i))
    }

    my_array.sort(sortNumber)
    console.log(my_array[1])
}
