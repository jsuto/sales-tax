#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This app prints the receipt of the purchased products"""
import re
import sys


IMPORT_TAX = 0.05
SALES_TAX = 0.1
ROUND_FACTOR = 0.05


def round_tax(value):
    """Calculate the rounded tax value"""

    # Based on the pattern in the example outputs rounding always
    # go higher, so 10.01 is rounded to 10.05 and not to 10.00.
    #
    # The algorithm to get the rounded value:
    #
    # 11.8125 % 0.05 = 0.0125 (We need to round this value up)
    # 0.05 - 0.0125 = 0.0375 (Calculate how much to increase)
    # 11.8125 + 0.0375 = 11.85 (The rounded value)

    # Workaround for the floating point arithmetic imprecision, eg.
    # 10 % 0.05 = 0.04999999999999945

    offset = 0

    if value > 0:
        offset = ROUND_FACTOR - round(value % ROUND_FACTOR, 4)

    return round(value + offset, 2)


def calc_import_tax(product, price):
    """Calculate the imported tax value"""
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
    """The main function"""
    total_sales_tax = 0
    total_price = 0

    for (amount, product, price) in read_products():
        basic_sales_tax = calc_basic_sales_tax(product, price)
        import_tax = calc_import_tax(product, price)

        sales_tax = round_tax(basic_sales_tax + import_tax)

        total_sales_tax += sales_tax

        # Product gross price = amount * (price + sales tax)
        gross_price = amount * (price + sales_tax)
        total_price += gross_price

        print(f"{amount} {product}: {gross_price:.2f}")

    # Print only two digits of the fraction part of the price
    print(f"Total sales tax: {total_sales_tax:.2f}")
    print(f"Total: {total_price:.2f}")


if __name__ == '__main__':
    main()
