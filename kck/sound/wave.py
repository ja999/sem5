#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import math
import sys
import scipy.io.wavfile

def nearest_two(x):
  return math.pow(2, math.ceil(math.log(x) / math.log(2)))

logging = True

def print_this(*arg):
  if logging:
    to_print = ''
    for i in arg:
      to_print += str(i) + ' '
    print to_print

print_this('reading file...')
# w, array2 = scipy.io.wavfile.read('1khz.wav')
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
low_freq_ign = 60
hi_freq_ign = 10000
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

subplot(211)
print_this('skipping first subplot...')

signal1 = fft(signal)
signal1 = abs(signal1)
print_this('calculated fft!')

print_this('cutting fft...')
print_this(floor(float(signal1.size) / float(2.0)))
if signal1.size / 2 == n / 2:
  signal_cut = signal1[:(signal1.size / 2)]
else:
  signal_cut = signal1[:(signal1.size / 2) - 1]
signal_cut = np.concatenate((np.zeros(low_freq_ign * (Tend - Tstart)), signal_cut[(low_freq_ign * (Tend - Tstart)):(hi_freq_ign * (Tend - Tstart))], np.zeros(signal_cut.size - (hi_freq_ign * (Tend - Tstart))+1)), axis = 0)
max_amp = np.amax(signal_cut)
max_amp_freq = np.argmax(signal_cut) / (Tend - Tstart)

print_this('frequency with maximum amplitude:')
print_this(max_amp_freq)

thresh = max_amp * thresh_factor

signal_filtered = np.array([ind / (Tend - Tstart) for ind, s in enumerate(signal_cut) if s > thresh])

print_this('filtered sgnal aray:')
print_this(signal_filtered)
print_this(signal_filtered.size)

if signal_filtered[0] > 180:
  res = 'K'
else:
  res = 'M'

status = int(res in sys.argv[1])
print_this(status, res, sys.argv[1])
exit(status)

# plotting...
# subplot(212)
# signal1[0] = 0
print_this('downsampling for plot...')
# a = linspace(0, w / 2, n / (2 * plot_factor), False, False)
# signal_to_plot = signal_cut[0::plot_factor]
# signal_to_plot = signal_to_plot[:a.size]
print_this('plotting...')
# stem(a, signal_to_plot, '-*')
print_this('plotted! :)')

# show()
