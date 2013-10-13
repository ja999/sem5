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
  def get_last_row(self, tab):
    last = tab[-1]
    del last[0:2]
    last = [float(x) * 100 for x in last]
    return last

class ReadControl:
  def openo(self, siema):
    tab = []
    with open(siema, "rb") as readfile:
      args = csv.reader(readfile, delimiter=',')
      for row in args:
        tab.append(row)
    return tab

def main():
  chart = Chart()
  fig = plt.figure(figsize=(13.4, 6.7))
  ax = fig.add_subplot(121)
  ax2 = ax.twiny()
  ax.set_xlim([0, 500])
  ax2.set_xlim([0, 200])
  ax.set_ylim([0.6, 1.0])
  ax2.set_xticks(range(0, 201, 40))
  plt.grid()
  markers = ['o', 'd', 'v', 's', 'D']
  boxy = []
  names = []
  for i, a in enumerate(glob.glob("*.csv")):
    tab = ReadControl().openo(a)
    all_points = chart.get_all(tab)
    last_row = chart.get_last_row(tab)
    boxy.append(last_row)
    b = a.replace(".csv", "", 1)
    names.append(b)
    artist = ax.plot(all_points[1], all_points[2], marker = markers[i], label = b)
    artist[0].set_markevery(25)
  ax.legend(loc = 4)
  ax.set_xlabel("Rozegranych gier (x1000)")
  ax2.set_xlabel("Pokolenie")
  plt.ylabel("Odsetek wygranych gier")

  ax3 = fig.add_subplot(122)
  ax3.grid()
  plt.xticks(range(1, 6), names, rotation = 45)
  ax3.yaxis.tick_right()
  ax3.set_ylim([60, 100])
  avgs = []
  boxy.reverse()
  for i in boxy:
    avgs.append(sum(i) / len(i))
  ax3.boxplot(boxy, 1)
  ax3.scatter([1, 2, 3, 4, 5], avgs)

  plt.savefig("a.pdf")
  plt.close()

if __name__ == "__main__":
  main()
