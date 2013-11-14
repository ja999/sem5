#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import colorsys
from skimage import filter, measure, data, io, img_as_float, morphology
from skimage.morphology import disk, square
from skimage.filter.rank import autolevel

def invert(v):
  return 1.0 - v

def process(v):
  th = np.amin(v) + ((np.amax(v) - np.amin(v)) / 3.1)
  binary = (v < th)
  binary = morphology.closing(binary, square(2))
  binary = morphology.closing(binary, square(16))
  return binary

def main():
  for i in range(0, 13):
    fig = plt.figure()
    if i < 10:
      fname = 'samolot0' + str(i) + '.jpg'
    else:
      fname = 'samolot' + str(i) + '.jpg'
    original = data.imread(fname)
    im = data.imread(fname, as_grey = True)
    binary = process(im)
    io.imshow(original)
    contours = measure.find_contours(binary, 0.9)
    for n, contour in enumerate(contours):
      plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
    plt.axis('image')
    plt.xticks([])
    plt.yticks([])
    plt.savefig(str(i) + '_5.jpg', bbox_inches = 0, frameon = False)


if __name__ == "__main__":
  main()
