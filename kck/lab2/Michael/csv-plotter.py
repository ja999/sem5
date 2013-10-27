#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import Controller

CSV_DIRECTORY = "ipd-choices-9-005"
OUTPUT_FILE = "ja_chce_piatke.pdf"

LOW_XLABEL = "Rozegranych gier (x1000)"
TOP_XLABEL = "Pokolenie"
YLABEL = "Odsetek wygranych gier [%]"

MARKERS = ('o', 'v', 'D', 's', 'd')
COLORS = ('b', 'g', 'r', 'k', 'm')
LABEL_ROTATION = 20
LEGEND_LOC = 4
LEGEND_SIZE = 12
LEGEND_ALPHA = 0.75
FIG_SIZE = (10, 6.7)
    
def main():
  controller = Controller(CSV_DIRECTORY, OUTPUT_FILE)
  controller.parse_files()
  controller.plot(LOW_XLABEL, TOP_XLABEL, YLABEL, markers = MARKERS, colors = COLORS, label_rotation = LABEL_ROTATION, loc = LEGEND_LOC, alpha = LEGEND_ALPHA, legend_size = LEGEND_SIZE, figsize = FIG_SIZE)

if __name__ == "__main__":
  main()

