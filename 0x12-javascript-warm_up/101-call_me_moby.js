#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let count = 0;
  while (count < x) {
    theFunction();
    count++;
  }
};
