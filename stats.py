from math import isfinite
from statistics import mean as _mean


def mean(values):
    """Return the finite arithmetic mean, or reject invalid inputs."""
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
    return _mean(values)
