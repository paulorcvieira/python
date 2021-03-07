import unittest
from src.soma import soma


class TestSoma(unittest.TestCase):
    def test_return_sum_10_10(self):
        self.assertEqual(soma(10, 10), 20)

    def test_return_sum_20_10(self):
        self.assertEqual(soma(20, 10), 30)
