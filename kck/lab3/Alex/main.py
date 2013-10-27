#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import csv
import glob
from scipy import randn
from matplotlib import rc
from matplotlib import colors
import colorsys

class Gradients:
  def gradient_hsl_for_map(self, v, maxi, mini):
    a = v / 145
    a = 1 - a
    return colorsys.hls_to_rgb(0.6 * a, 0.4, 1)
  def peak(self, t, h):
    maxis = []
    for i in t:
      maxis.append(max(i))
    return max(maxis)
  def dump(self, tab, h):
    maxis = []
    for i in range(0, int(h)-1):
      maxis.append(min(tab[i]))
    return min(maxis)
  def draw(self, tab, maxi, mini, w, h):
    img = np.zeros((int(w), int(h), 3))
    for i in range(0, int(w)-1):
      for j in range(0, int(h)-1):
        # print i, j
        img[i, j] = self.gradient_hsl_for_map(tab[i][j], maxi, mini)
    im = plt.imshow(img, aspect='auto')
    plt.show()
    plt.savefig('my-map.pdf')

class ReadControl:
  def openo(self, siema):
    tab = []
    temp = []
    with open(siema, "rb") as readfile:
      args = csv.reader(readfile, delimiter=' ')
      for row in args:
        for i in row:
          temp.append(float(i))
        tab.append(temp)
        temp = []
    return tab
  def process(self, tab):
    wynik = []
    for i in range(1, int(tab[0][1])):
      wynik.append(tab[i])
    return wynik

def main():
  read = ReadControl()
  grad = Gradients()
  tab = read.openo("dane")
  w = tab[0][0]
  h = tab[0][1]
  tab = read.process(tab)
  maxi = grad.peak(tab, h)
  mini = grad.dump(tab, h)
  grad.draw(tab, maxi, mini, w, h)


if __name__ == "__main__":
  main()
