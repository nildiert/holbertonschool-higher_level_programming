#!/usr/bin/node
exports.converter = function (base) {
  function converterFunction (num) {
    return num.toString(base);
  }
  return converterFunction;
};
