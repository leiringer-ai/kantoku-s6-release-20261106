exports.median = function median(values) {
  if (!Array.isArray(values) || values.length === 0) {
    throw new TypeError('median requires a nonempty array of finite numbers');
  }

  const sorted = values.slice();
  for (const value of sorted) {
    if (!Number.isFinite(value)) {
      throw new TypeError('median requires finite numbers');
    }
  }
  sorted.sort((a, b) => a - b);

  const middle = Math.floor(sorted.length / 2);
  if (sorted.length % 2 === 1) {
    return sorted[middle];
  }

  const lower = sorted[middle - 1];
  const upper = sorted[middle];
  const sum = lower + upper;
  // Divide first only when needed, so tiny values retain their precision.
  return Number.isFinite(sum) ? sum / 2 : lower / 2 + upper / 2;
};
