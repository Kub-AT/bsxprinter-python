#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from bsxprinter.generator import ReceiptGenerator, Receipt
from bsxprinter.formatters import FileFormatter, XMLFormatter


def single_example():
    receipt = Receipt('receipt-id-0', cash=500)
    for i in range(1, 5):
        receipt.add_item('Item {}'.format(i), 20*i, 1, 23)

    ff_gen = ReceiptGenerator(FileFormatter)
    xml_gen = ReceiptGenerator(XMLFormatter)
    print(ff_gen.generate(receipt))
    print('\n')
    print(xml_gen.generate(receipt))


def multi_example():
    ff_gen = ReceiptGenerator(FileFormatter)
    xml_gen = ReceiptGenerator(XMLFormatter)
    rec1 = Receipt('receipt-id-1', card=500)
    rec1.add_item('Item 1', 99, 1, 23).add_item('Item 2', 149.95, 2, 23)

    rec2 = Receipt('receipt-id-2', cash=100)
    rec2.add_item('Item A', 23, 3, 23)
    rec2.add_item('Item B', 11, 1, 8)

    receipts = [rec1, rec2]

    print(ff_gen.generate(receipts))
    print('\n')
    print(xml_gen.generate(receipts))

if __name__ == '__main__':
    single_example()

    print('\n--mutliple--\n')
    multi_example()
