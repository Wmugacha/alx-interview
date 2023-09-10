#!/usr/bin/node
const argv = process.argv;
const filmApiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieUrl = `${filmApiUrl}${argv[2]}/`;

const request = require('request');

request(movieUrl, function (error, response, body) {
  if (error == null) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (characters && characters.length > 0) {
      const characterLimit = characters.length;
      fetchCharacters(0, characters[0], characters, characterLimit);
    }
  } else {
    console.log(error);
  }
});

function fetchCharacters (index, characterUrl, characters, limit) {
  if (index === limit) {
    return;
  }
  request(characterUrl, function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      index++;
      fetchCharacters(index, characters[index], characters, limit);
    } else {
      console.error('Error:', error);
    }
  });
}
