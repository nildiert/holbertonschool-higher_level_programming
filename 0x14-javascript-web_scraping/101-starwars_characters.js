#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      request(characterUrl, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
