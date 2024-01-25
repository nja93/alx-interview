#!/usr/bin/env node
// Write a script that prints all characters of a Star Wars movie:
// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
// Display one character name by line in the same order of the list “characters” in the /films/ response
// URL: https://swapi-api.alphacoders.com/api/films/:id

const request = require('request');

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

async function orderedResponses (urls) {
  const responses = [];
  for (const url of urls) {
    const response = await get(url);
    responses.push(response);
  }
  return responses;
}

get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2])
  .then((res) => {
    orderedResponses(JSON.parse(res).characters)
      .then((responses) => {
        responses.forEach((response) => console.log(JSON.parse(response).name));
      })
      .catch((error) => {
        console.error(error);
      });
  });
