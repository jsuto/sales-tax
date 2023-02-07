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
    for (amount, product, price) in read_products():
        print(amount, product, price)


if __name__ == '__main__':
    main()
