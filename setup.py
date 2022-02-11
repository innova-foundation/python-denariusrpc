#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-innovarpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Innova',
    long_description=open('README.rst').read(),
    author='Original - buzzkillb | Innova - CircuitBreaker',
    author_email='<development@innova-foundation.com>',
    maintainer='CircuitBreaker',
    maintainer_email='<development@innovacoin.io>',
    url='http://www.github.com/innova-foundation/python-innovarpc',
    packages=['innovarpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
