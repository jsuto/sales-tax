import receipt
import unittest


class TestReceipt(unittest.TestCase):

    def test_import_tax(self):
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

if __name__ == "__main__":
    unittest.main()
