#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from bsxprinter.generator import ReceiptGenerator, Receipt
from bsxprinter.formatters import FileFormatter, XMLFormatter


if __name__ == '__main__':
    receipt = Receipt()
    receipt.add_item('Item 1', 99, 1, 23).add_item('Item 2', 149.95, 2, 23)

    gen = ReceiptGenerator(FileFormatter)
    print(gen.generate(receipt, cash=500))
    print(gen.generate(receipt, card=700))

    print('\n---\n')

    gen = ReceiptGenerator(XMLFormatter)
    print(gen.generate(receipt, rid='receipt-id-123', cash=500))
