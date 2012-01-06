#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyremotecv - remotecv client for python
# https://github.com/globocom/pyremotecv/wiki

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 globo.com timehome@corp.globo.com

import datetime

from tornado import ioloop
import bson
import zmq
import zmq.eventloop


class PyRemoteCV(object):
    zmq_ctx = None

    @classmethod
    def get_context(cls):
        if cls.zmq_ctx is None:
            cls.zmq_ctx = zmq.Context()

        return cls.zmq_ctx

    @classmethod
    def async_detect_all(cls, server, image_size, image_bytes, callback, image_mode='RGB', timeout=20):
        cls.async_detect('all', server, image_size, image_bytes, callback, image_mode, timeout)

    @classmethod
    def async_detect_faces(cls, server, image_size, image_bytes, callback, image_mode='RGB', timeout=20):
        cls.async_detect('face', server, image_size, image_bytes, callback, image_mode, timeout)

    @classmethod
    def async_detect_features(cls, server, image_size, image_bytes, callback, image_mode='RGB', timeout=20):
        cls.async_detect('feat', server, image_size, image_bytes, callback, image_mode, timeout)

    @classmethod
    def async_detect(cls, action, server, image_size, image_bytes, callback, image_mode, timeout):
        loop = ioloop.IOLoop.instance()

        def on_result(data):
            loop.remove_timeout(timeout_handle)
            stream.close()
            features = bson.loads(data[0])['points']
            if features:
                callback(features)
            else:
                callback([])

        def on_timeout(self):
            self.stream.close()
            self.callback(None)

        ctx = cls.get_context()

        socket = ctx.socket(zmq.REQ)
        socket.connect(server)
        socket.setsockopt(zmq.LINGER, 0)

        timeout_handle = ioloop.add_timeout(datetime.timedelta(seconds=timeout), on_timeout)
        stream = zmq.eventloop.zmqstream.ZMQStream(socket, ioloop)
        stream.on_recv(on_result)

        msg = { 
            'type': action,
            'size': image_size,
            'mode': image_mode,
            'image': image_bytes
        }

        stream.send(bson.dumps(msg))


