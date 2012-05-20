#!/usr/bin/env python

import setuptools

import sigproc

setuptools.setup(
  author='Alexandru Marinescu <almarinescu@gmail.com>',
  entry_points={'console_scripts': 
      ['launch-sigproc = sigproc.control:run_app']},
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
