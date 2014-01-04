#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile

w, array = scipy.io.wavfile.read('err.wav')

print w
print [s[0] for s in array]

# array = genfromtxt('spots.txt')

# w = max(array) * 2 # częstotliwość próbkowania [Hz]
T = 1

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

# f = lambda t : sin(100*2*pi*t)    # def. funkcji
# print f(t)
# signal = f(t)                 # funkcja spróbkowana

# size = array.size
# print array[floor(size*0.34)]
# print t

# # f = lambda t : array[floor(size*t)] # def. funkcji
# # signal = f(t) # funkcja spróbkowana
signal = []
for i in t:
  signal.append(array[floor(size*i)])

subplot(211)
# print signal[0]
# var = linspace(0, array.size, n, endpoint=False)
# plot(var, signal, '*')

signal1 = fft(signal)
signal1 = abs(signal1)        # moduł

subplot(212)
# signal1[0] = 0
a = linspace(0, w, n, False, False)
stem(a, signal1, '-*')

show()
