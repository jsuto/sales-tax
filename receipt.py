#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys


IMPORT_TAX = 0.05
SALES_TAX = 0.1
ROUND_FACTOR = 0.05


def calc_import_tax(product, price):
    if re.search(r'imported ', product, re.I):
        return price * IMPORT_TAX
    return 0


def calc_basic_sales_tax(product, price):
    """
    We allow case insensitivity for the product name
    """

    if re.search(r'(book|chocolate|pills)', product, re.I):
        return 0
    return price * SALES_TAX


def read_products():
    """
    Read product info from stdin, 1 product per line.
    Fields are separated by semicolon (;), eg.
    1;book;14.90

    We also assume that each line is valid, and
    has the required fields with appropriate values.
    """
    products = []

    for line in sys.stdin:
        (amount, product, price) = line.rstrip().split(';')
        products.append((int(amount), product, float(price)))

    return products


def main():
    total_sales_tax = 0
    total_price = 0

    for (amount, product, price) in read_products():
        print(amount, product, price)
        basic_sales_tax = calc_basic_sales_tax(product, price)
        import_tax = calc_import_tax(product, price)

        sales_tax = basic_sales_tax + import_tax

        total_sales_tax += sales_tax

        # Product gross price = amount * (price + sales tax)
        gross_price = amount * (price + sales_tax)
        total_price += gross_price

    print('Total sales tax:', total_sales_tax)
    print('Total:', total_price)


if __name__ == '__main__':
    main()
