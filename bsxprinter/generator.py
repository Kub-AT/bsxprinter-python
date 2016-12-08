#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from decimal import Decimal

class Generator(object):
    formatter = None

    def __init__(self, formatter):
        self.formatter = formatter()

    def gen_receipt(self, items, **kwargs):
        return self.formatter.gen_receipt(items, **kwargs)


class Receipt(object):
    items = None

    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add_item(self, name, price, amount, vat):
        self.items.append({
            'name': str(name),
            'price': Decimal(price).quantize(Decimal('.00')),
            'amount': Decimal(amount).quantize(Decimal('0')),
            'vat': Decimal(vat).quantize(Decimal('0'))
        })
        return self
