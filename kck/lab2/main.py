#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import csv
import glob
from scipy import randn

class Chart:
  def get_point(self, args):
    try:
      population = int(args[0])
      games = int(args[1])
      siema = [float(x) for x in args[2:]]
      val = sum(siema) / len(siema)
      ret = [population, games, val]
      # print "sukces"
      # print ret
      return ret
    except:
      0
  def get_all(self, full):
    try:
      self.pops = []
      self.gs = []
      self.vals = []
      for a in full:
        if a[0] != "generation":
          r = self.get_point(a)
          self.pops.append(r[0])
          self.gs.append(r[1] / 1000)
          self.vals.append(r[2])
      ret = [self.pops, self.gs, self.vals]
      return ret
    except:
      0

class ReadControl:
  def __init__(self):
    0
  def openo(self, siema):
    tab = []
    with open(siema, "rb") as readfile:
      args = csv.reader(readfile, delimiter=',')
      for row in args:
        tab.append(row)
    return tab

def main():
  fig = plt.figure(figsize=(6.7, 6.7))
  ax = fig.add_subplot(111)
  ax2 = ax.twiny()
  ax.set_xlim([0, 500])
  ax2.set_xlim([0, 200])
  ax.set_ylim([0.6, 1.0])
  plt.grid()
  for a in glob.glob("*.csv"):
    tab = ReadControl().openo(a)
    all_points = Chart().get_all(tab)
    b = a.replace(".csv", "", 1)
    ax.plot(all_points[1], all_points[2], label = b)
  ax.legend(loc = 4)
  ax.set_xlabel("Rozegranych gier (x1000)")
  ax2.set_xlabel("Pokolenie")
  plt.ylabel("Odsetek wygranych gier")


  plt.savefig("a.pdf")
  # plt.show()
  plt.close()


if __name__ == "__main__":
  main()
