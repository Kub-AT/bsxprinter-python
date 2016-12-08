#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BSXGenerator(object):
    formatter = None

    def __init__(self, formatter):
        self.formatter = formatter()

    def genReceipt(self, items, **kwargs):
        return self.formatter.genReceipt(items, **kwargs)


class BSXPrinterReceipt(object):
    items = None

    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def addItem(self, name, price, amount, vat):
        self.items.append({
            'name': str(name),
            'price': str(price),
            'amount': str(amount),
            'vat': str(vat)
        })
        return self
