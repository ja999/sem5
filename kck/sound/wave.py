#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

# print 'reading file...'
# w, array2 = scipy.io.wavfile.read('1khz.wav')
w, array2 = scipy.io.wavfile.read('train/007_M.wav')
# print 'read!'

# print 'sampling frequency:'
# print w

# print 'splitting channels...'
if array2[0].size == 1:
  array = array2
else:
  array = np.array([s[0] for s in array2])
# print 'splitted!'

cut = 0.5
start = 0.4
size = array.size
plot_factor = 100
low_freq_ign = 60
hi_freq_ign = 10000

T = size / w
# print 'array size:'
# print size
# print 'time of the file:'
# print T

Tend = cut * T
Tstart = start * T
# print 'time taken into account:'
# print (Tend - Tstart)

n = (Tend - Tstart) * w
t = linspace(Tstart, Tend, n, endpoint=False)

# print 'time  points for X: '
# print t

# print 'cutting parts from signal...'
signal = []
for i in range(int(start*size), int(cut*size)):
  signal.append(array[i])
# print 'fragmented!'

subplot(211)
# print 'skipping first subplot...'

signal1 = fft(signal)
signal1 = abs(signal1)
# print 'calculated fft!'

# print 'cutting fft...'
# print floor(float(signal1.size) / float(2.0))
if signal1.size / 2 == n / 2:
  signal_cut = signal1[:(signal1.size / 2)]
else:
  signal_cut = signal1[:(signal1.size / 2) - 1]
signal_cut = np.concatenate((np.zeros(low_freq_ign * (Tend - Tstart)), signal_cut[(low_freq_ign * (Tend - Tstart)):(hi_freq_ign * (Tend - Tstart))], np.zeros(signal_cut.size - (hi_freq_ign * (Tend - Tstart))+1)), axis = 0)
max_amp = np.amax(signal_cut)
max_amp_freq = np.argmax(signal_cut) / (Tend - Tstart)

# print 'frequency with maximum amplitude:'
# print max_amp_freq

thresh = max_amp * 0.1

signal_filtered = np.array([ind / (Tend - Tstart) for ind, s in enumerate(signal_cut) if s > thresh])

# print 'filtered sgnal aray:'
# print signal_filtered
# print signal_filtered.size

if signal_filtered[0] > 180:
  print 'k'
else:
  print 'm'

# plotting...
# subplot(212)
# signal1[0] = 0
# print 'downsampling for plot...'
# a = linspace(0, w / 2, n / (2 * plot_factor), False, False)
# signal_to_plot = signal_cut[0::plot_factor]
# signal_to_plot = signal_to_plot[:a.size]
# print 'plotting...'
# stem(a, signal_to_plot, '-*')
# print 'plotted! :)'

# show()
