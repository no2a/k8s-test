#!/usr/bin/env python

import os

import gevent
import gevent.pywsgi


def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return 'Hello, world'


if __name__ == '__main__':
    http_server = gevent.pywsgi.WSGIServer(('', 3000), app)
    http_server.serve_forever()
