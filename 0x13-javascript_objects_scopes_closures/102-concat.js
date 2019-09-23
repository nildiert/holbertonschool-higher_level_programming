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
const file1 = './fileA';
const file2 = './fileB';
const appendFile = './fileC';
readAppend(file1, appendFile);
readAppend(file2, appendFile);
