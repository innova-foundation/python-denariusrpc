#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-innovarpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Innova',
    long_description=open('README.rst').read(),
    author='Original - buzzkillb | Innova - CircuitBreaker88',
    author_email='<circuitbreaker@innova.io>',
    maintainer='circuitbreaker88',
    maintainer_email='<circuitbreaker@innova.io>',
    url='http://www.github.com/innova-foundation/python-innovarpc',
    packages=['innovarpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
