"""Module for testing the Receipt app"""
import unittest
import receipt


class TestReceipt(unittest.TestCase):
    """Class for testing the Receipt app"""

    def test_import_tax(self):
        """Test the import tax calculator function"""
        data = [
            ('imported box of chocolates', 10),
            ('book', 10),
            ('a box of imported chocolates', 10),
            ('Imported Chocolates', 10),
        ]

        expected_results = [
            0.5,
            0,
            0.5,
            0.5
        ]

        results = []

        for (product, price) in data:
            results.append(receipt.calc_import_tax(product, price))

        self.assertEqual(expected_results, results)

    def test_basic_sales_tax(self):
        """Test the basic sales tax calculator function"""
        data = [
            ('imported box of chocolates', 10),
            ('watch', 10),
            ('a box of imported chocolates', 10),
            ('Imported Chocolates', 10),
        ]

        expected_results = [
            0,
            1,
            0,
            0
        ]

        results = []

        for (product, price) in data:
            results.append(receipt.calc_basic_sales_tax(product, price))

        self.assertEqual(expected_results, results)

    def test_round_tax(self):
        """Test the tax rounding function"""
        data = [
            10,
            10.01,
            10.18,
            10.25,
            10.48,
            10.50,
            10.511,
            10.60,
            10.682,
            10.75,
            10.99,
            7.625,
            11.8125,
        ]

        expected_results = [
            10,
            10.05,
            10.2,
            10.25,
            10.5,
            10.5,
            10.55,
            10.6,
            10.7,
            10.75,
            11.00,
            7.65,
            11.85
        ]

        results = []

        for value in data:
            results.append(receipt.round_tax(value))

        self.assertEqual(expected_results, results)


if __name__ == "__main__":
    unittest.main()
