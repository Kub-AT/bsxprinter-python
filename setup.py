#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import bsxprinter

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='bsxprinter',
    version=bsxprinter.__version__,
    description='BSX Printer Python Lib',
    url='https://github.com/Kub-AT/bsxprinter-python',
    download_url='https://github.com/Kub-AT/bsxprinter-python/releases',
    license="MIT",
    packages=find_packages(exclude=['docs', 'tests*']),
    package_data={},
    zip_safe=True,
    install_requires=requirements,
    keywords='bsxprinter thermal posnet novitus',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    extras_require={
        'tests': [
            'nose',
            'pytest',
            'pytest-cov',
            'pytest-pep8',
        ],
        'docs': [
            'sphinx==1.2.3',  # autodoc was broken in 1.3.1
            'sphinxcontrib-napoleon',
            'sphinx_rtd_theme',
            'numpydoc',
        ],
    }
)
