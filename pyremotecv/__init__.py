#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyremotecv - remotecv client for python
# https://github.com/globocom/pyremotecv/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 globo.com timehome@corp.globo.com

from redis import Redis

# version is here for people to query for the library version upon install
from pyremotecv.version import version, Version, __version__

class PyRemoteCV:

    def __init__(self, host, port, db, password):
        from pyremotecv.unique_queue import UniqueQueue
        redis = Redis(host=host, port=port, db=db, password=password)
        self.queue = UniqueQueue(server=redis)

    def async_detect(self, class_name, queue_name, args=[], key=None):
        self.queue.enqueue_unique_from_string(class_name, queue_name,
                args=args,
                key=key)
