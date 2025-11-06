#!/usr/bin/node

const { argv } = require('node:process');

// Les arguments réels commencent à l’index 2
if (argv.length > 2) {
  console.log('Argument found');
  // si non argv
} else {
  console.log('No argument');
}
