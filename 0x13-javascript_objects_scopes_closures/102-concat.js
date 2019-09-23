#!/usr/bin/node
var fs = require('fs');
if (process.argv.length === 5) {
  const file1 = process.argv[2];
  const file2 = process.argv[3];
  const appendFile = process.argv[4];
  const contentFileA = fs.readFileSync(file1, 'utf-8');
  const contentFileB = fs.readFileSync(file2, 'utf-8');
  fs.writeFileSync(appendFile, contentFileA + contentFileB);
}
