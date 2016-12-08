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
import bsxprinter
receipt = bsxprinter.Receipt()
receipt.addItem('Item 1', 99, 1, 23).addItem('Item 2', 149.95, 2, 23)

gen = BSXGenerator(FileFormatter)
print(gen.genReceipt(receipt, cash=500))
print(gen.genReceipt(receipt, card=700))

gen = Generator(XMLFormatter)
print(gen.genReceipt(receipt, rid='receipt-id-123', cash=500))

```