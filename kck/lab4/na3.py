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
from skimage import filter, measure, data, io, img_as_float, data_dir
from skimage.morphology import disk
from skimage.filter.rank import autolevel
from skimage.io import MultiImage
from mpl_toolkits.axes_grid import AxesGrid

def invert(v):
  return 1.0 - v

def process(v):
  v = v ** 4
  th = np.amin(v) + ((np.amax(v) - np.amin(v)) / 16.0)
  binary = (v > th)
  return binary

def main():
  imgs = MultiImage(data_dir + '/multipage.tif')

  for a, i in zip(range(0, 4), [1, 9, 7, 8]):
    fig = plt.figure()
    ax = fig.add_axes([-0.1, -0.1, 1.2, 1.2])
    # ax.set_axis_off()
    im = data.imread('samolot0' + str(i) + '.jpg', as_grey = True)
    im = invert(im)
    im = process(im)
    out = np.ones_like(im)
    io.imshow(out)
    contours = measure.find_contours(im, 0.9)
    for n, contour in enumerate(contours):
      plt.plot(contour[:, 1], contour[:, 0], linewidth=2, color = 'white')
    plt.savefig(str(a) + '.jpg', bbox_inches = 0, frameon = False)

  fig = plt.figure()
  grid = AxesGrid(fig, rect = (1, 1, 1), nrows_ncols = (2, 2), axes_pad = 0.1)

  for i in range(0, 4):
    frame = data.imread(str(i) + '.jpg')
    grid[i].imshow(frame)
    grid[i].set_xticks([])
    grid[i].set_yticks([])

  plt.savefig('na3.jpg')
if __name__ == "__main__":
  main()
