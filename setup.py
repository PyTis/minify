#!/usr/bin/env python

import os
from setuptools import setup
from minify import minify

__curdir__ = os.path.abspath(os.path.dirname(__file__))

setup(
    name='minify',
    version=minify.__version__,
    author=minify.__author__,
    author_email='Josh.Lee@PyTis.com;Josh.Lee@FranklinTempleton.com',
    description='Developer tool to recursively minify CSS and JS',
    py_modules=['minify.minify'],  # Reference your standalone minify module
    install_requires=[
        'rjsmin==1.2.2',
    ],
    license="PyTis LICENSE 3.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'License :: GNU Public License',
        'Operating System :: OS Independent',
        'Programming Language :: CSS',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    scripts=[
			os.path.abspath(os.path.join(__curdir__, 'bin/mini')),
			os.path.abspath(os.path.join(__curdir__, 'bin/minify')),
    ],
#    entry_points={
#        'console_scripts': [
#            'mini=bin.minify',  # Assuming main() is in minify.py and is the entry point
#        ],
#    },
)
