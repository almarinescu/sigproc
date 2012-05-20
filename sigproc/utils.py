from __future__ import print_function
import os
import logging
import sqlite3

import bottle
import mako.lookup
import mako.template
import memcache

import sigproc.model as model

templates_lookup = mako.lookup.TemplateLookup(
		directories=[os.path.join('sigproc', 'templates')],
		module_directory=os.path.join('sigproc', 'templates','modules'))

memcache_client = memcache.Client(['127.0.0.1:1122'])
dbcache_client = model.DbCache()

def mako_template(lookup, templateName):
	return lookup.get_template(templateName)

def ck_response():
  low = bottle.request.query['low']
  high = bottle.request.query['high']

  return '/response-{0:.2f}-{1:.2f}'.format(float(low), float(high))

def ck_index():
  return '/index/template'

def cache_response(cache_client, key_cache):
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
