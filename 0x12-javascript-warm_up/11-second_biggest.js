#!/usr/bin/node
let numsPassed = process.argv.splice(2);
if (numsPassed.length < 2) {
  console.log(0);
} else {
  console.log(numsPassed);
  numsPassed = numsPassed.map(num => parseInt(num, 10));
  numsPassed.sort((a, b) => b - a);
  const secondLarge = numsPassed[1];
  console.log(secondLarge);
}
