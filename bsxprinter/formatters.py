#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import abc
import datetime
import six

from decimal import Decimal

from lxml import etree


@six.add_metaclass(abc.ABCMeta)
class FormatterBase(object):

    @abc.abstractmethod
    def generate(self, items, **kwargs):
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

    def create_cmd(self, cmd, params=None):
        result = '{0}{1}'.format(self.separator, cmd)
        if params:
            if isinstance(params, list):
                result += '{0}{1}'.format(self.separator,
                                          self.separator.join((map(self.xstr, params))))
            else:
                result += '{0}{1}'.format(self.separator, str(params))
        return result

    def generate(self, receipts):
        command = ''
        for receipt in receipts:
            items = receipt.items
            command += self.create_cmd('RECEIPT')
            total = Decimal(0)
            for item in items:
                params = self._get_item_params(item)
                command += self.create_cmd('ITEM', params)
                total += params[4]

            commit_params = [total.quantize(Decimal('.00')), receipt.cash, receipt.card]
            command += self.create_cmd('COMMIT', commit_params)
        """ Plik .in na FTP powinnien konczyć się poleceniem EXECUTE"""
        command += self.create_cmd('EXECUTE')
        return command

    def _get_item_params(self, item):
        return [
            item['name'],
            item['price'],
            item['amount'],
            item['vat'],
            item['price'] * item['amount']
        ]


class TCPFormatter(FormatterBase):
    """
    Generowany format służy do komunikacji z BSX Printer za pośrednictwem TCP.
    """
    separator = '#'

    def generate(self, receipts):
        """TODO"""


class XMLFormatter(FormatterBase):
    """
    Generowany format służy do komunikacji z BSX Printer za pośrednictwem odpytywanej
    końcówki API XML, z której to co pewien czas BSX Printer stara się pobrać nowe recepty
    do wydruku.
    """

    def generate(self, receipts):
        header = '<?xml version="1.0" encoding="utf-8"?>\n\n'
        root_xml = etree.Element('root')
        receipts_xml = etree.Element('receipts')

        for receipt in receipts:
            items = receipt.items

            total = Decimal(0)
            xml_items = []
            for item in items:
                item_params = self._item_params(item)
                total += Decimal(item_params['total'])
                xml_items.append(etree.Element('item', **item_params))

            receipt_xml = etree.Element('receipt', **self._receipt_params(receipt, total))
            receipt_xml.extend(xml_items)

            receipts_xml.append(receipt_xml)
        root_xml.append(receipts_xml)

        return header + etree.tostring(root_xml, pretty_print=True).decode('utf-8')

    def _receipt_params(self, receipt, total):
        params = {
            'id': str(receipt.rid),
            'total': str(total),
            'date': str(datetime.date.today())
        }
        if receipt.cash:
            params['cash'] = str(receipt.cash)
        if receipt.card:
            params['visa'] = str(receipt.card)
        if receipt.rest:
            params['rest'] = str(receipt.rest)
        return params

    def _item_params(self, item):
        return {
            'name': str(item['name']),
            'price': str(item['price']),
            'quantity': str(item['amount']),
            'total': str(item['price'] * item['amount']),
            'vatrate': str(item['vat'])
        }
