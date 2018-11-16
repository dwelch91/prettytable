#!/usr/bin/env python
from setuptools import setup

setup(
    name='prettytable',
    version='0.8.0',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing'
    ],
    license="BSD (3 clause)",
    description='A simple Python library for easily displaying tabular data in a visually appealing ASCII table format',
    author='Luke Maurits',
    author_email='luke@maurits.id.au',
    url='http://code.google.com/p/prettytable',
    py_modules=['prettytable'],
    test_suite="prettytable_test"
)
