#!/usr/bin/node
/* File to append */
const fs = require('fs');
const path = './';
const contentFileA = fs.readFileSync(path + process.argv[2], 'utf-8');
const contentFileB = fs.readFileSync(path + process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], contentFileA + contentFileB);
