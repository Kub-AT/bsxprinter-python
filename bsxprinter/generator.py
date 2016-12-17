#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from decimal import Decimal


class ReceiptGenerator(object):
    formatter = None

    def __init__(self, formatter):
        self.formatter = formatter()

    def generate(self, receipts):
        if not isinstance(receipts, list):
            receipts = [receipts]
        for rec in receipts:
            assert isinstance(rec, Receipt)
        return self.formatter.generate(receipts)


class Receipt(object):
    rid = None
    cash = None
    card = None
    rest = None
    items = None

    def __init__(self, rid, cash=None, card=None, rest=None, **kwargs):
        self.rid = rid
        self.cash = Decimal(cash).quantize(Decimal('.00')) if cash else None
        self.card = Decimal(card).quantize(Decimal('.00')) if card else None
        self.rest = Decimal(rest).quantize(Decimal('.00')) if rest else None
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
