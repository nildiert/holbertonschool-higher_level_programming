#!/usr/bin/node
var fs = require('fs');
const contentFileA = fs.readFileSync(process.argv[2], 'utf-8');
const contentFileB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], contentFileA + contentFileB);
