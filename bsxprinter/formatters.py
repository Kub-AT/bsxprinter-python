#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import abc
import datetime
import six

from lxml import etree


@six.add_metaclass(abc.ABCMeta)
class FormatterBase(object):

    @abc.abstractmethod
    def genReceipt(self, items, **kwargs):
        """Metoda generująca dane paragonu"""
        return

    def xstr(self, s):
        if s is None:
            return ''
        return str(s)


class FileFormatter(FormatterBase):
    """
    Generowany format służy do komunikacji z BSX Printer za pośrednictwem FTP lub innej
    przestrzeni współdzielone. Wygenerowany output można zapisać jako plik .in na takiej
    przestrzeni.
    """
    separator = '#'

    def createCmd(self, cmd, params=None):
        result = '{0}{1}'.format(self.separator, cmd)
        if params:
            if isinstance(params, list):
                result += '{0}{1}'.format(self.separator,
                                          self.separator.join((map(self.xstr, params))))
            else:
                result += '{0}{1}'.format(self.separator, str(params))
        return result

    def genReceipt(self, items, cash=None, card=None):
        command = ''
        command += self.createCmd('RECEIPT')
        total = 0
        for item in items:
            command += self.createCmd('ITEM', self._getItemParams(item))
            total += float(item['price']) * \
                float(item['amount'])  # TODO Decimal

        command += self.createCmd('COMMIT', [total, cash, card])
        """ Plik .in na FTP powinnien konczyć się poleceniem EXECUTE"""
        command += self.createCmd('EXECUTE')
        return command

    def _getItemParams(self, item):
        item_params = [item['name'], item[
            'price'], item['amount'], item['vat']]
        item_params.append(float(item['price']) * float(item['amount']))
        return item_params


class TCPFormatter(FormatterBase):
    """
    Generowany format służy do komunikacji z BSX Printer za pośrednictwem TCP.
    """
    separator = '#'

    def genReceipt(self, items, cash=None, card=None):
        """TODO"""


class XMLFormatter(FormatterBase):
    """
    Generowany format służy do komunikacji z BSX Printer za pośrednictwem odpytywanej
    końcówki API XML, z której to co pewien czas BSX Printer stara się pobrać nowe recepty
    do wydruku.
    """

    def genReceipt(self, items, rid, cash=None, card=None):
        header = '<?xml version="1.0" encoding="utf-8"?>\n\n'
        root = etree.Element('root')
        receipts = etree.Element('receipts')

        total = 0
        xml_items = []
        for item in items:
            item_params = self._itemParams(item)
            total += float(item_params['total'])
            xml_items.append(etree.Element('item', **item_params))

        receipt = etree.Element(
            'receipt', **self._receiptParams(rid, total, cash, card))
        receipt.extend(xml_items)

        receipts.append(receipt)
        root.append(receipts)

        return header + etree.tostring(root, pretty_print=True).decode('utf-8')

    def _receiptParams(self, rid, total, cash=None, card=None, rest=None):
        params = {
            'id': str(rid),
            'total': str(total),
            'date': datetime.datetime.now().strftime('%Y-%m-%d')
        }
        if cash:
            params['cash'] = str(cash)
        if card:
            params['visa'] = str(card)
        if rest:
            params['rest'] = str(rest)
        return params

    def _itemParams(self, item):
        return {
            'name': item['name'],
            'price': item['price'],
            'quantity': item['amount'],
            'total': str(float(item['price']) * float(item['amount'])),
            'vatrate': item['vat']
        }
