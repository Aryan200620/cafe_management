import unittest

def calculate_bill(price, quantity):
    return price * quantity

def validate_quantity(quantity, available_stock):
    return quantity > 0 and quantity <= available_stock

class TestCafeRegression(unittest.TestCase):

    def test_bill_calculation(self):
        self.assertEqual(calculate_bill(100, 2), 200)

    def test_bill_with_multiple_items(self):
        self.assertEqual(calculate_bill(50, 3), 150)

    def test_zero_quantity(self):
        self.assertEqual(validate_quantity(0, 10), False)

    def test_valid_stock(self):
        self.assertEqual(validate_quantity(3, 10), True)

    def test_excess_stock(self):
        self.assertEqual(validate_quantity(12, 10), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)

