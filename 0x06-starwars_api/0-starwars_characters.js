#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';
const args = process.argv.slice(2);
if (args.length >= 1) {
  const movieId = args[0];
  request(`${BASE_URL}/films/${movieId}`, (err, resp, body) => {
    if (err || resp.statusCode !== 200) {
      console.log(err);
    }

    const charactersURL = JSON.parse(body).characters;
    const promises = charactersURL.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, resp, body) => {
          if (err || resp.statusCode !== 200) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      });
    });

    Promise.all(promises)
      .then((names) => console.log(names.join('\n')))
      .catch((err) => console.log(err));
  });
}
