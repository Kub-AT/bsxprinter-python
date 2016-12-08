# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from bsxprinter.generator import Generator, Receipt
from bsxprinter.formatters import XMLFormatter


class TestStringMethods(unittest.TestCase):

    def test_receipt_add_item(self):
        receipt = Receipt()
        receipt.addItem('Item 1', 19, 1, 23)
        self.assertEqual(len(receipt.items), 1)
        receipt.addItem('Item 2', 99, 1, 23).addItem('Item 3', 149.95, 2, 23)
        self.assertEqual(len(receipt.items), 3)

if __name__ == '__main__':
    unittest.main()
