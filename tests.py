#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

import unittest

from bsxprinter.generator import ReceiptGenerator, Receipt
from bsxprinter.formatters import XMLFormatter


class ReceiptTest(unittest.TestCase):

    def test_it_should_add_items(self):
        receipt = Receipt(1)
        self.assertEqual(receipt.items, [])
        receipt.add_item('Item 1', 19, 1, 23)
        self.assertEqual(len(receipt.items), 1)
        receipt.add_item('Item 2', 99, 1, 23).add_item('Item 3', 149.95, 2, 23)
        self.assertEqual(len(receipt.items), 3)

    def test_is_should_iter_over_items(self):
        receipt = Receipt(1)
        receipt.add_item('Item 2', 99, 1, 23).add_item('Item 3', 149.95, 2, 23)
        try:
            iter(receipt)
        except TypeError:
            self.fail("Receipt should be iterable")


class GeneratorTest(unittest.TestCase):

    def test_it_should_set_formatter_instance(self):
        gen = ReceiptGenerator(XMLFormatter)
        self.assertIsInstance(gen.formatter, XMLFormatter)


if __name__ == '__main__':
    unittest.main()
