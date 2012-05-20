#!/usr/bin/env python

import numpy as np
import scipy.signal as signal

def fir_coeffs(cutoff_freqs,
    filter_opts={'window':'blackmanharris','numtaps':100, 'nyq': 1.0}):
  if not isinstance(cutoff_freqs, list):
    raise TypeError('cutoff_freqs must be a list of frequencies.')
  return signal.firwin(cutoff=cutoff_freqs, **filter_opts)

def bandpass_filter(low_coeffs, high_coeffs):
  return spectral_invert(low_coeffs+high_coeffs)

def spectral_invert(coeffs):
  n = len(coeffs)
  inv_coeffs = -coeffs[:]
  # inv_coeffs[n/2] = inv_coeffs[n/2] + 1

  return inv_coeffs

def freq_resp(coeffs, denom=1):
  w, h = signal.freqz(coeffs, denom)
  return w, h

def impulse_resp(coeffs, denom=1):
  l = len(coeffs)
  impulse = np.array([1.] + [0.] * (l-1))
  x = np.arange(0,l)
  response = signal.lfilter(coeffs, denom, impulse)

  return x, response

def step_resp(coeffs, denom=1):
  samples, response = impulse_resp(coeffs, denom=1)
  return samples, np.cumsum(response)

def rescale(data, sub=0, div=1):
  data -= sub
  data /= div

  return data

def in_db(sin):
  return 20 * np.log10(np.abs(sin))

