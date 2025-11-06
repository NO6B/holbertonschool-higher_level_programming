#!/usr/bin/node

// Les argument
const { argv } = require('node:process');

// Vérifie si un argument existe
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
