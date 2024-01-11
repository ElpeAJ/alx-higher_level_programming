#!/usr/bin/node
let numsPassed = process.argv.splice(2);
let numArray = [];
if (numsPassed.length < 2) {
  console.log(0);
} else {
  //console.log(typeof(numsPassed));
  console.log(numsPassed);
  numsPassed = numsPassed.map(num => parseInt(num, 10));
  //console.log(numsPassed);
  numsPassed.sort((a, b) => b - a);
  const secondLarge = numsPassed[1];
  console.log(secondLarge);
 /* for (let num = 0; num < numsPassed.length; num++){
  numArray.push(numsPassed[num]);
  console.log(numArray);
  }*/
}
