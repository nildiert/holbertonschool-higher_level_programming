#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const myObject = {};
    const data = JSON.parse(body);
    for (const i of data) {
      if (i.completed) {
        if (i.userId in myObject) {
          myObject[i.userId] += 1;
        } else {
          myObject[i.userId] = 1;
        }
      }
    }
    console.log(myObject);
  }
});
