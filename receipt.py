#!/usr/bin/python3
# -*- coding: utf-8 -*-

IMPORT_TAX = 0.05
SALES_TAX = 0.1
ROUND_FACTOR = 0.05


def calc_import_tax(product, price):
    if re.search(r'imported ', product, re.I):
        return price * IMPORT_TAX
    return 0


if __name__ == '__main__':
    main()