#!/usr/bin/env python3
"""
Copyright (c) 2017-2025 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='samsung_print',
    version='0.1.0',
    description='Python API for interacting with devices from Samsung.',
    long_description=long_description,
    url='https://github.com/fabaff/samsung_print',
    download_url='https://github.com/fabaff/samsung_print/releases',
    author='Fabian Affolter',
    author_email='fabian@affolter-engineering.ch',
    license='MIT',
    install_requires=['aiohttp', 'async_timeout', 'PyYAML'],
    packages=['samsung_print'],
    python_requires='>=3.10',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.10',
        'Topic :: Utilities',
    ],
)
