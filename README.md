# Small data tools

Three independently usable components share `catalog.json`, a JSON object whose
`features` array advertises their names. The repository starts with unimplemented
stubs. Add the selected component's feature without dropping other features.

* `stats.py`: `mean(values)` for a nonempty sequence of finite real numbers.
  Preserve fractional and mixed-sign results, accept integers/floats, reject empty,
  booleans, nonnumeric values and nonfinite numbers with ValueError or TypeError.
  It must handle very large finite values when their mathematical mean is finite.
  Advertise `mean`. Declared component check: `mise run test-python`.
* `median.cjs`: export `median(values)` for a nonempty array of finite numbers.
  Sort numerically without mutating input, return fractional results for even
  lengths, reject empty/non-array/nonnumeric/nonfinite inputs with an Error.
  Avoid overflowing the midpoint of two equal large finite values. Advertise
  `median`. Declared component check: `mise run test-javascript`.
* `lines.sh`: stdin-only POSIX shell CLI that prints the count of logical lines,
  including a nonempty final unterminated line. Preserve blank lines; empty
  input is zero. Reject arguments with a diagnostic and nonzero exit. Advertise
  `lines`. Declared component check: `mise run test-shell`.

The complete default check is `mise run test` (`sh tests/all.sh`), which connects
all three language suites and validates the complete catalog. A contribution can
use its declared component check; the integrated result must pass the full suite.
Keep the tools dependency-free apart from their declared language runtimes.
