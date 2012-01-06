#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyremotecv - remotecv client for python
# https://github.com/globocom/pyremotecv/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 globo.com timehome@corp.globo.com


def install_io_loop():
    try:
        from zmq.eventloop import ioloop
        ioloop.install()
    except ImportError:
        pass


