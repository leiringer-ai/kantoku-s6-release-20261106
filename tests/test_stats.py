import json, math, unittest
from fractions import Fraction
from stats import mean

class MeanTests(unittest.TestCase):
    def test_fractions(self):
        self.assertEqual(mean([1, 2]), 1.5)
        self.assertEqual(mean([-2, 1, 3]), 2 / 3)
    def test_rejection(self):
        for values in [[], [True], ["2"], [float("nan")], [float("inf")]]:
            with self.subTest(values=values), self.assertRaises((ValueError, TypeError)):
                mean(values)
    def test_large_finite_mean(self):
        self.assertEqual(mean([1e308, 1e308]), 1e308)
    def test_advertised(self):
        with open("catalog.json") as f:
            self.assertIn("mean", json.load(f)["features"])

    def test_integers_and_floats(self):
        values = [1, 2.5, -2]
        self.assertEqual(mean(values), 0.5)
        self.assertEqual(values, [1, 2.5, -2])
        self.assertEqual(mean((3.5,)), 3.5)

    def test_additional_invalid_values(self):
        for value in [False, None, 2j, -math.inf, "2"]:
            with self.subTest(value=value), self.assertRaises((ValueError, TypeError)):
                mean([1, value])

    def test_large_cancellation(self):
        self.assertEqual(mean([1e308, 1e308, -1e308, -1e308, 5]), 1)
        self.assertEqual(mean([1e308, 1e308, -1e308]), 1e308 / 3)

    def test_small_finite_mean(self):
        smallest = math.ulp(0.0)
        self.assertEqual(mean([smallest, smallest]), smallest)

    def test_large_integers(self):
        large = 10 ** 400
        self.assertEqual(mean([large, large]), large)
        self.assertEqual(mean([large, -large, 3]), 1)

    def test_large_mixed_mean(self):
        large = 10 ** 400
        self.assertEqual(mean([large, 0.0]), large // 2)
        self.assertEqual(mean([-large, 0.0]), -large // 2)

    def test_large_fractional_mean(self):
        large = 10 ** 400
        self.assertEqual(mean([large, 1]), Fraction(large + 1, 2))
        self.assertEqual(mean([large, 0.5]), Fraction(2 * large + 1, 4))
