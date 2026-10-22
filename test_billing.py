
import unittest

def calculate_bill(price, quantity):
    return price * quantity

class TestBillCalculation(unittest.TestCase):

    def test_valid_bill(self):
        self.assertEqual(calculate_bill(100, 2), 200)

    def test_zero_quantity(self):
        self.assertEqual(calculate_bill(100, 0), 0)

    def test_multiple_items(self):
        self.assertEqual(calculate_bill(50, 3), 150)

if __name__ == "__main__":
    unittest.main()
