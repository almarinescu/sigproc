#!/usr/bin/env python

import ast

import sqlobject

# Create a connection to an in-memory SQLite3 db.
sqlobject.sqlhub.processConnection = sqlobject.connectionForURI(
    'sqlite:/:memory:', 
    autoCommit=True)

class Cache(sqlobject.SQLObject):
  '''
  The cache table has two columns: key and value.

  The table is indexed by the key.
  '''
  key = sqlobject.StringCol()
  value = sqlobject.StringCol()

  keyIndex = sqlobject.DatabaseIndex('key')

class DbCache(object):
  '''
  A wrapper class which exposes the interface needed by the caching
  decorator.
  '''

  def get(self, key, conversion_fn=None):
    '''
    Extract the value associated with a given key.

    If the key doesn't exist return None. If the key exists try to parse
    the value string as a python base data type. If the parsing fails, just
    return the string stored in db.
    '''
    res = list(Cache.select(Cache.q.key == key))
    if len(res) == 0:
      return None
  
    try: 
      return ast.literal_eval(res[0].value)
    except SyntaxError:
      return res[0].value

  def set(self, key, value):
    db_row = Cache(key=key, value=str(value))

# The caching table only gets created if it doesn't exist.
Cache.createTable(ifNotExists=True)
