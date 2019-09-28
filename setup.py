#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-denariusrpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Denarius',
    long_description=open('README.rst').read(),
    author='buzzkillb',
    author_email='<buzz@denarius.io>',
    maintainer='buzzkillb',
    maintainer_email='<jgarzik@pobox.com>',
    url='http://www.github.com/buzzkillb/python-denariusrpc',
    packages=['denariusrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)
