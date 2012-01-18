#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyremotecv - remotecv client for python
# https://github.com/globocom/pyremotecv/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 globo.com timehome@corp.globo.com


# version is here for people to query for the library version upon install
from pyremotecv.version import version, Version, __version__
from pyremotecv.unique_queue import UniqueQueue


class PyRemoteCV:
    queue = UniqueQueue()

    @classmethod
    def async_detect(cls, class_name, queue_name, args=[], key=None):
        cls.queue.enqueue_unique_from_string(class_name, queue_name,
                args=args,
                key=key)
