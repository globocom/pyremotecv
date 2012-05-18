#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyremotecv - remotecv client for python
# https://github.com/globocom/pyremotecv/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 globo.com timehome@corp.globo.com

from setuptools import setup, find_packages
from pyremotecv.version import version

description = "pyremotecv is a client library for remotecv (https://github.com/globocom/remotecv/wiki)."

setup(
    name = 'pyremotecv',
    version = version,
    description = description,
    long_description = description,
    keywords = 'facial feature detection opencv remote zeromq socket',
    author = 'Time Home',
    author_email = 'timehome@corp.globo.com',
    url = 'https://github.com/globocom/pyremotecv',
    license = 'MIT',
    classifiers = ['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.6',
    ],

    packages = find_packages(),

    install_requires=[
        "pyres>=1.2,<1.3"
    ],

)


