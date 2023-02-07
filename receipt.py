#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


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


def main():
    pass


if __name__ == '__main__':
    main()
