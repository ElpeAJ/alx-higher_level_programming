#!/usr/bin/node
const argOne = process.argv[2];
if (argOne !== undefined) {
  console.log(argOne);
} else {
  console.log('No argument');
}
