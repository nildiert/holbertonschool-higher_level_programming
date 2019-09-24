#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const key of results) {
      const character = key.characters;
      for (const item of character) {
        if (item.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
