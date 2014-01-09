#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import math
import sys
import scipy.io.wavfile

logging = False
plotting = False

def nearest_two(x):
  return math.pow(2, math.ceil(math.log(x) / math.log(2)))

def print_this(*arg):
  if logging:
    to_print = ''
    for i in arg:
      to_print += str(i) + ' '
    print to_print

def unfiltered_precessing(signal, sensitivity):
  amps_array_male = np.array([s[1] for s in signal if s[0] > 80 and s[0] < 160 ])
  amps_array_female = np.array([s[1] for s in signal if s[0] > 170 and s[0] < 220 ])
  if amps_array_female.size > 0 and amps_array_male.size > 0:
    print_this('certainty coefficient:')
    print_this(np.amax(amps_array_male) / np.amax(amps_array_female))
    if (np.amax(amps_array_male) / np.amax(amps_array_female)) < sensitivity:
      return True
    else:
      return False
  return False

print_this('reading file...')
w, array2 = scipy.io.wavfile.read(str(sys.argv[1]))
print_this('read!')

print_this('sampling frequency:')
print_this(w)

print_this('splitting channels...')
if array2[0].size == 1:
  array = array2
else:
  array = np.array([s[0] for s in array2])
print_this('splitted!')

cut = 1
start = 0
size = array.size
plot_factor = 100
low_freq_ign = 80
hi_freq_ign = 8000
thresh_factor = 0.15

T = size / w
print_this('array size:')
print_this(size)
print_this('time of the file:')
print_this(T)

Tend = cut * T
Tstart = start * T
print_this('time taken into account:')
print_this((Tend - Tstart))

n = (Tend - Tstart) * w
t = linspace(Tstart, Tend, n, endpoint=False)

print_this('time  points for X: ')
print_this(t)

print_this('cutting parts from signal...')

signal = []
for i in range(int(start*size), int(cut*size)):
  signal.append(array[i])
signal = np.concatenate((signal, np.zeros(nearest_two(size) - size)), axis = 0)
print_this(signal.size)
scale = signal.size / size
T *= scale
Tend *= scale
Tstart *= scale

print_this('fragmented!')

signal1 = fft(signal)
signal1 = abs(signal1)
print_this('calculated fft!')

print_this('cutting fft...')
if signal1.size / 2 == n / 2:
  signal_cut = signal1[:(signal1.size / 2)]
else:
  signal_cut = signal1[:(signal1.size / 2) - 1]
# Tend = Tend / 2
if signal_cut.size - (hi_freq_ign * (Tend - Tstart)) + 1 > 0:
  signal_cut = np.concatenate((np.zeros(low_freq_ign * (Tend - Tstart)), signal_cut[(low_freq_ign * (Tend - Tstart)):(hi_freq_ign * (Tend - Tstart))], np.zeros(signal_cut.size - (hi_freq_ign * (Tend - Tstart)) + 1)), axis = 0)
else:
  signal_cut = np.concatenate((np.zeros(low_freq_ign * (Tend - Tstart)), signal_cut[(low_freq_ign * (Tend - Tstart)):(hi_freq_ign * (Tend - Tstart))], np.zeros(signal_cut.size - ((hi_freq_ign * (Tend - Tstart)) / 2) + 1)), axis = 0)
max_amp = np.amax(signal_cut)
max_amp_freq = np.argmax(signal_cut) / (Tend - Tstart)

print_this('frequency with maximum amplitude:')
print_this(max_amp_freq)

thresh = max_amp * thresh_factor

signal_filtered = np.array([ind / (Tend - Tstart) for ind, s in enumerate(signal_cut) if s > thresh])
signal_unfiltered = np.array([[ind / (Tend - Tstart), s] for ind, s in enumerate(signal_cut) if s > thresh])

print_this('filtered signal aray:')
print_this(signal_filtered)
print_this(signal_filtered.size)

print_this('unfiltered signal array:')
print_this(signal_unfiltered[0])
print_this(signal_unfiltered[1])
print_this(signal_unfiltered.size)

print_this('first known frequency:')
print_this(signal_filtered[0])

if signal_filtered[0] > 180:
  res = 'K'
else:
  if unfiltered_precessing(signal_unfiltered, 0.9):
    res = 'K'
  else:
    res = 'M'

status = int(res in sys.argv[1]) + 2
print status, res, sys.argv[1]
if not plotting:
  exit(status)

if plotting:
  subplot(211)
  plot(array)

  subplot(212)
  signal1[0] = 0
  print_this('downsampling for plot...')
  a = linspace(0, w / 2, n / (2 * plot_factor), False, False)
  signal_to_plot = signal_cut[0::plot_factor]
  signal_to_plot = signal_to_plot[:a.size]
  print_this('plotting...')
  stem(a, signal_to_plot, '-*')
  print_this('plotted! :)')

  show()
