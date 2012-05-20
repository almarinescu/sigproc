#!/usr/bin/env python

import setuptools

import sigproc

setuptools.setup(
  author='Alexandru Marinescu <almarinescu@gmail.com>',
  install_requires=[
      'bottle', 
      'gunicorn',
      'mako', 
      'python-memcached',
      'scipy',
      'sqlobject'],
  name='sigproc',
  packages=setuptools.find_packages(),
  test_suite='sigproc.test',
  version=sigproc.__version__)
