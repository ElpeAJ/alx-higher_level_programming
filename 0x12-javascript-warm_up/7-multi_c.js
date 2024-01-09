#!/usr/bin/node
const numArgc = parseInt(process.argv[2]);
if (isNaN(numArgc)) {
  console.log('Missing number of occurrences');
} else {
  for (let argc = 0; argc < numArgc; argc++) {
    console.log('C is fun');
  }
}
