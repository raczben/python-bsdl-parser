#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,

    entry_points={
        'console_scripts': [
            'bsdl2json = bsdl_parser.bsdl2json:main',
        ],
    },
    
    packages = ['bsdl_parser']
)