from fractions import Fraction
from math import isfinite
from statistics import mean as _mean


def mean(values):
    """Return the mean, retaining an exact result if it exceeds float range."""
    values = list(values)
    if not values:
        raise ValueError("mean requires at least one value")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("mean requires integers or floats")
        if isinstance(value, float) and not isfinite(value):
            raise ValueError("mean requires finite values")
    # The standard library accumulates exact ratios, avoiding sum overflow
    # and preserving cancellation before converting the final result.
    try:
        return _mean(values)
    except OverflowError:
        # Mixed inputs and fractional integer means can exceed float range.
        # Keep their exact value using only standard-library arithmetic.
        result = sum((Fraction(value) for value in values), Fraction()) / len(values)
        return result.numerator if result.denominator == 1 else result
