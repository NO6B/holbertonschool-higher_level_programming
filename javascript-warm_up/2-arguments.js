#!/usr/bin/node

// Les arguments réels commencent à l’index 2

const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
