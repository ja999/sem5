#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controller import Controller

IMAGE_FILE_SCHEME = '../images/samolot%02d.jpg'
OUTPUT_FILE_SCHEME = 'pr_%02d.jpg'

PLANES = range(0, 13)

def main():
  controller = Controller(IMAGE_FILE_SCHEME, PLANES, OUTPUT_FILE_SCHEME)
  controller.parse_files()
  controller.process_files()
  controller.plot_files()

if __name__ == '__main__':
  main()

