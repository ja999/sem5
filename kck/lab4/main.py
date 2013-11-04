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
from skimage import filter, measure, data, io, img_as_float
from skimage.morphology import disk
from skimage.filter.rank import autolevel

def main():
  original = data.imread('samolot03.jpg')
  ima = data.imread('samolot04.jpg', as_grey = True)
  im = ima**6
  thresh = filter.threshold_otsu(ima)
  binary = (ima > thresh)
  io.imshow(binary)
  contours = measure.find_contours(binary, 0.1)
  print len(contours)
  # colorki = ['green', 'red', 'blue', 'black', 'yellow', 'magenta', 'white', 'cyan', 'brown', 'silver']
  for n, contour in enumerate(contours):
    plt.plot(contour[:, 1], contour[:, 0], linewidth=2)
  plt.axis('image')
  plt.xticks([])
  plt.yticks([])
  plt.show()


if __name__ == "__main__":
  main()
