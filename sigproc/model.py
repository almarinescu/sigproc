#!/usr/bin/env python

import ast

import sqlobject

sqlobject.sqlhub.processConnection = sqlobject.connectionForURI(
    'sqlite:/:memory:', 
    autoCommit=True)

class Cache(sqlobject.SQLObject):
  key = sqlobject.StringCol()
  value = sqlobject.StringCol()

  keyIndex = sqlobject.DatabaseIndex('key')

class DbCache(object):
  def get(self, key, conversion_fn=None):
    res = list(Cache.select(Cache.q.key == key))
    if len(res) == 0:
      return None
  
    try: 
      return ast.literal_eval(res[0].value)
    except SyntaxError:
      return res[0].value

  def set(self, key, value):
    db_row = Cache(key=key, value=str(value))

Cache.createTable(ifNotExists=True)
