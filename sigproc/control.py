#!/usr/bin/env python

from __future__ import print_function

import logging
import os
import pprint

import bottle
import gunicorn
import numpy as np

import sigproc.sig as sig
import sigproc.utils as utils

main_app = bottle.Bottle()

@main_app.route('/response')
@utils.cache_response(utils.dbcache_client, utils.ck_response)
def response():
  '''
  Simulate a bandpass filter and return the frequency, step and impulse
  response as a JSON dictionary.
  '''
  # Simple arguments validation.
  try:
    low_freq = float(bottle.request.query['low'])
    high_freq = float(bottle.request.query['high'])
  except ValueError:
    low_freq = 0.1
    high_freq = 0.9

  # Create the low-pass, the high-pass filters and combine them into a
  # bandpass filter.
  lpf_coeffs = sig.fir_coeffs([low_freq])
  hpf_coeffs = sig.spectral_invert(sig.fir_coeffs([high_freq]))
  bpf_coeffs = sig.bandpass_filter(lpf_coeffs, hpf_coeffs)

  # Frequency response.
  freq_resp_w, freq_resp_h = sig.freq_resp(bpf_coeffs)
  freq_resp_w = sig.rescale(freq_resp_w, 0, max(freq_resp_w)).tolist()
  freq_resp_hdb = sig.in_db(freq_resp_h).tolist()

  # Step response.
  step_samples, step_response = map(
      lambda x: x.tolist(), 
      sig.step_resp(bpf_coeffs))

  # Impulse response.
  impulse_samples, impulse_response = map(
      lambda x: x.tolist(),
      sig.impulse_resp(bpf_coeffs))

  # Return the results in a dictionary which will automatically be
  # converted to JSON by Bottle.
  return {
      'freq_response': zip(freq_resp_w, freq_resp_hdb),
      'step_response': zip(step_samples, step_response),
      'impulse_response': zip(impulse_samples, impulse_response)
  }

@main_app.route('/favicon.ico')
def favicon():
  '''Serve the favicon icon.'''
	return bottle.static_file('favicon.ico', os.path.join('sigproc', 'static'))

@main_app.route('/static/<filename:path>')
def static_files(filename):
  '''Serve static files from the /static directory.'''
	return bottle.static_file(filename, os.path.join('sigproc', 'static'))

@main_app.route('/')
@utils.cache_response(utils.memcache_client, utils.ck_index)
def index():
  '''Render and return the main page template.'''
  index_template = utils.mako_template(utils.templates_lookup, 'index.mako')
  return index_template.render(title='Frequency, step and impulse response.')

def run_app():
  '''Start the main application on top of GUnicorn server.'''
  bottle.run(
      main_app, 
      host='0.0.0.0',
      port='8080',
      server='gunicorn')

if __name__ == '__main__':
  run_app()
