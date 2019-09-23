#!/usr/bin/node
var fs = require('fs');
if (process.argv.length === 5) {
  const contentFileA = fs.readFileSync(process.argv[2], 'utf-8');
  const contentFileB = fs.readFileSync(process.argv[3], 'utf-8');
  fs.writeFileSync(process.argv[4], contentFileA + contentFileB);
}
