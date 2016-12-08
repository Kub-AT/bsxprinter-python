#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from bsxprinter.generator import Generator, Receipt
from bsxprinter.formatters import FileFormatter, XMLFormatter


if __name__ == '__main__':
    receipt = Receipt()
    receipt.addItem('Item 1', 99, 1, 23).addItem('Item 2', 149.95, 2, 23)

    gen = Generator(FileFormatter)
    print(gen.genReceipt(receipt, cash=500))
    print(gen.genReceipt(receipt, card=700))

    print('\n---\n')

    gen = Generator(XMLFormatter)
    print(gen.genReceipt(receipt, rid='receipt-id-123', cash=500))
