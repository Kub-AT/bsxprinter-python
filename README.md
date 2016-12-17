# bsxprinter-python
BSXPrinter Python Lib

[![PyPI version](https://badge.fury.io/py/bsxprinter.svg)](https://badge.fury.io/py/bsxprinter)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Kub-AT/bsxprinter-python/master/LICENSE.md)
[![PyPI](https://img.shields.io/pypi/pyversions/bsxprinter.svg?maxAge=2592000)]()

[![Build Status](https://travis-ci.org/Kub-AT/bsxprinter-python.svg?branch=master)](https://travis-ci.org/Kub-AT/bsxprinter-python)
[![Coverage Status](https://coveralls.io/repos/github/Kub-AT/bsxprinter-python/badge.svg?branch=master)](https://coveralls.io/github/Kub-AT/bsxprinter-python?branch=master)


# Install

To install the most up to date release of this module via PyPi:

```pip install bsxprinter```

To install the master branch:

```pip install git+https://github.com/Kub-AT/bsxprinter-python.git```

or

```
git clone https://github.com/Kub-AT/bsxprinter-python.git
cd bsxprinter
python setup.py install
```


# Tests

```
make test
```

# Example

```python
from bsxprinter.generator import ReceiptGenerator, Receipt
from bsxprinter.formatters import FileFormatter, XMLFormatter

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

```
