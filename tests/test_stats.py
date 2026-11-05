import json, math, unittest
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
