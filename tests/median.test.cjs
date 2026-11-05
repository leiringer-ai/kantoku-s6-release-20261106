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
test('advertised', () => assert.ok(require('../catalog.json').features.includes('median')));
