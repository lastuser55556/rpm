import unittest
from decimal import Decimal
from billing import total


class BillingTests(unittest.TestCase):
    def test_discount(self):
        self.assertEqual(total(Decimal("49.90"), 3, 10), Decimal("134.73"))

    def test_half_cent_rounds_up(self):
        self.assertEqual(total(Decimal("1.01"), 1, 50), Decimal("0.51"))

    def test_full_discount(self):
        self.assertEqual(total(Decimal("50"), 1, 100), Decimal("0.00"))

    def test_invalid_arguments(self):
        for args in (("-1", 1, 0), ("1", 0, 0), ("1", 1, 101)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                total(Decimal(args[0]), *args[1:])


if __name__ == "__main__":
    unittest.main()
