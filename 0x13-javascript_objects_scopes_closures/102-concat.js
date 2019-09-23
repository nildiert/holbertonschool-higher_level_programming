#!/usr/bin/node
var fs = require('fs');

function readAppend (file, appendFile) {
  fs.readFile(file, function (err, data) {
    if (err) throw err;
    fs.appendFile(appendFile, data, function (err) {
      if (err) throw err;
    });
  });
}

const path = './';
const file1 = path + process.argv[2];
const file2 = path + process.argv[3];
const appendFile = path + process.argv[4];
if (process.argv.length === 5) {
  readAppend(file1, appendFile);
  readAppend(file2, appendFile);
}
