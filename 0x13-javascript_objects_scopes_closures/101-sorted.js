#!/usr/bin/node
const dict = require('./101-data').dict;
// let newDict = new Object();
const newDict = {};
for (const i in dict) {
  if (dict[i] in newDict) {
    newDict[dict[i]].push(i);
  } else {
    newDict[dict[i]] = [];
    newDict[dict[i]].push(i);
  }
}
console.log(dict);
console.log(newDict);
