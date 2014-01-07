#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

print 'reading file...'
w, array2 = scipy.io.wavfile.read('1khz.wav')
print 'read!'

print 'sampling frequency:'
print w

print 'splitting channels...'
if array2[0].size == 1:
  array = array2
else:
  array = np.array([s[0] for s in array2])
print 'splitted!'

cut = 0.5
start = 0.4
size = array.size

T = size / w
print 'array size:'
print size
print 'time of the file:'
print T

Tend = cut * T
Tstart = start * T
print 'time taken into account from file start:'
print T

n = (Tend - Tstart) * w        # liczba próbek
t = linspace(Tstart, Tend, n, endpoint=False) # punkty na osi OX [s]

# f = lambda t : sin(100*2*pi*t)    # def. funkcji
# print f(t)
# signal = f(t)                 # funkcja spróbkowana


# print array[floor(size*0.34)]
print 'time  points for X: '
print t

# # f = lambda t : array[floor(size*t)] # def. funkcji
# # signal = f(t) # funkcja spróbkowana
print 'cutting parts from signal...'
signal = []
for i in range(int(start*size), int(cut*size)):
  signal.append(array[i])
print 'fragmented!'

subplot(211)
# print signal[0]
# var = linspace(0, array.size, n, endpoint=False)
# plot(var, signal, '*')
print 'skipping first subplot...'

signal1 = fft(signal)
signal1 = abs(signal1)        # moduł
print 'calculated fft!'

print 'cutting fft...'
signal_cut = signal1[:(signal1.size / 2)]
max_amp_freq = np.argmax(signal_cut) / (Tend - Tstart)

print 'frequency with maximum amplitude:'
print max_amp_freq

subplot(212)
signal1[0] = 0
a = linspace(0, w / 2, n / 2, False, False)
print 'plotting...'
stem(a, signal_cut, '-*')
print 'plotted! :)'

show()
