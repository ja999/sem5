#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import Controller

FILE_NAME = "big.dem"
OUTPUT_FILE = "ja_chce_piatke_z_mapke.pdf"

def main():
  controller = Controller(FILE_NAME, OUTPUT_FILE)
  controller.parse_file()
  controller.plot()

if __name__ == "__main__":
  main()

