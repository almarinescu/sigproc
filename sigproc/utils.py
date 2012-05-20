#!/usr/bin/env python

from __future__ import print_function

import os
import logging
import socket
import sqlite3

import bottle
import mako.lookup
import mako.template
import memcache

import sigproc.model as model

# Look for templates in sigproc/templates and cache mako templates in 
# sigproc/templates/modules.
templates_lookup = mako.lookup.TemplateLookup(
		directories=[os.path.join('sigproc', 'templates')],
		module_directory=os.path.join('sigproc', 'templates','modules'))

# Make sure a memcache server is running and if so, create a memcache
# client instance. If no server can be found simply raise an Exception.
memcache_client = None
try:
  host = '127.0.0.1'
  port = 1122
  memcache_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  memcache_socket.connect((host, port))
  memcache_socket.shutdown(2)
  memcache_client = memcache.Client(['127.0.0.1:1122'])
except:
  raise Exception('No memcached server found @ {0}:{1}'.format(host, port))

# The database caching client.
dbcache_client = model.DbCache()

def mako_template(lookup, templateName):
  '''
  Return a mako template instance.
  
  This method checks the mako template in all directories specified by 
  the Mako TemplateLookup `lookup`.
  '''
	return lookup.get_template(templateName)

def cache_response(cache_client, key_cache):
  '''
  Caching decorator.

  This decorator receives a caching client and a caching function.
  The caching client must implement an interface which exposes two methods:
    * get(key) - returns the value associated with `key` if the key is
        cached or None.
    * set(key, value) - cache `value` at `key`.

  The `key_cache` method should return a string which corresponds to the
  key used to retrieve a certain value from cache.
  '''
  def decorator_wrapper(fn):
    def fn_wrapper(*args, **kw):
      key = key_cache()
      if cache_client.get(key) is not None:
        print('Serving results from cache for `{0}` @ `{1}` - {2}'
            .format(fn.__name__, key, cache_client))
        return cache_client.get(key)
      else:
        print('Calling `{0}` and caching result @ `{1}` in {2}'
            .format(fn.__name__, key, cache_client))
        res = fn(*args, **kw)
        cache_client.set(key, res)
        return res
    return fn_wrapper
  return decorator_wrapper

def ck_response():
  '''
  Use the `low` and `high` parameters to create the key-cache used to
  retrieve values for `/response` page.
  '''
  low = bottle.request.query['low']
  high = bottle.request.query['high']

  return '/response-{0:.2f}-{1:.2f}'.format(float(low), float(high))

def ck_index():
  '''HTML template pages are always cached using the path they are
  rendering with `/template` appended at the end.
  '''
  return '/index/template'
