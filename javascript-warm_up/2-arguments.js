#!/usr/bin/node

const { argv } = require('node:process');

// Les arguments réels commencent à l’index 2
if (argv.length < 0) {
  console.log('No argument');
} else if (argv.length > 1) {
  console.log('Argument found');
// si non argv
} else {
  console.log('Argument found');
}
