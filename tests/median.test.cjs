const test = require('node:test');
const assert = require('node:assert/strict');
const {median} = require('../median.cjs');
test('numeric fractional median without input mutation', () => {
  const input=[10, 2, -1, 3];
  assert.equal(median(input), 2.5);
  assert.deepEqual(input,[10, 2, -1, 3]);
  assert.equal(median([12, 3, 2]),3);
});
test('invalid inputs reject', () => {
  for(const value of [[], null, {}, [NaN], [Infinity], ['2'], [true]]) {
    assert.throws(() => median(value));
  }
});
test('large finite midpoint', () => assert.equal(median([1e308, 1e308]),1e308));
test('midpoint handles finite extremes and tiny values', () => {
  assert.equal(median([Number.MAX_VALUE, Number.MAX_VALUE]), Number.MAX_VALUE);
  assert.equal(median([-Number.MAX_VALUE, -Number.MAX_VALUE]), -Number.MAX_VALUE);
  assert.equal(median([-Number.MAX_VALUE, Number.MAX_VALUE]), 0);
  assert.equal(median([Number.MIN_VALUE, Number.MIN_VALUE]), Number.MIN_VALUE);
  assert.equal(median([Number.MIN_VALUE, 2 * Number.MIN_VALUE]), 2 * Number.MIN_VALUE);
});
test('frozen arrays and singleton values are supported', () => {
  assert.equal(median(Object.freeze([10, 2, 3])), 3);
  assert.equal(median([-2.5]), -2.5);
});
test('missing elements and other invalid values reject', () => {
  for (const value of ['123', [undefined], [null], [-Infinity], Array(1), [1, , 3]]) {
    assert.throws(() => median(value), Error);
  }
});
test('advertised', () => assert.ok(require('../catalog.json').features.includes('median')));
