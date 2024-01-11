#!/usr/bin/node
const numArgc = parseInt(process.argv[2]);
if (isNaN(numArgc)) {
  console.log('Missing size');
} else {
  for (let rargc = 0; rargc < numArgc; rargc++) {
    for (let argc = 0; argc < numArgc; argc++) {
      console.log('X');
    }
    console.log('');
  }
}
