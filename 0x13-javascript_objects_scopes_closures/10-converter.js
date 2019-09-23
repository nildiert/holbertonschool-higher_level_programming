#!/usr/bin/node
exports.converter = function (base) {
    if (typeof base != 'undefined') {
	converter.number = base
    } else {
	return parseInt(converter.number, base)
    }

}
