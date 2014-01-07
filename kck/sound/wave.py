#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

print 'reading file...'
w, array2 = scipy.io.wavfile.read('err.wav')
print 'read!'

print 'sampling frequency:'
print w

print 'splitting channels...'
array = np.array([s[0] for s in array2])
print 'splitted!'

cut = 0.1
start = 0
size = array.size

T = size / w
print 'array size:'
print size
print 'time of the file:'
print T

T = cut * T
print 'time taken into account from file start:'
print T

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

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

subplot(212)
signal1[0] = 0
a = linspace(0, w, n, False, False)
print 'plotting...'
stem(a, signal1, '-*')
print 'plotted! :)'

show()
