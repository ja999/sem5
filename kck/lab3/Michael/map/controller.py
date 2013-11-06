import matplotlib.pyplot as plt
from colorful_map import ColorfulMap
from map_input import MapInput
import colorsys
import math

def norm_cut(arg):
  return min(1, max(0, arg))

class Controller:
  def __init__(self, input_filename, output_filename):
    self.output_filename = output_filename
    self.input_filename = input_filename
    self.colorful_map = None

  def parse_file(self):
    self.colorful_map = ColorfulMap(sun_vector = (-1.0, 0.23, -1.0)).load(*MapInput(self.input_filename).parse())


  def gradient(self, v, s):
    s = norm_cut((s + 1) / 2)
    cs = 1 - abs(math.sin(3.1415 * (s - 0.5)))
    pf_s = norm_cut(0.1 + ((math.sin(3.1415 * (cs - 0.5)) + 1) / 2) ** 6)
    return colorsys.hsv_to_rgb((1 - v) / 2.75, norm_cut(2.3 * (norm_cut(pf_s - 0.25) ** 0.03) - 0.25), norm_cut(1.3 - pf_s))
    # return colorsys.hsv_to_rgb(1, 1, 1 - pf_s)
    # return colorsys.hsv_to_rgb(1, norm_cut(1 - s ** 20), norm_cut(0.1 + s ** 8))
    # return colorsys.hsv_to_rgb((1 - v) / 2.75, min(1, max(0, (1 - s ** 20))), s ** 0.05)
    # return colorsys.hsv_to_rgb((1 - v) / 2.75, min(1, max(0, (1 - (s + v * 0.01) * 1.64))) ** 0.02, s ** 0.05)
    # return colorsys.hsv_to_rgb(v, s, s)
    # return colorsys.hsv_to_rgb(v / 40, s, s)

  def plot(self):
    img = []
    for i in range(0, self.colorful_map.rows):
      row = []
      img.append(row)
      for j in range(0, self.colorful_map.cols):
        row.append(self.gradient(*self.colorful_map.color(i, j)))
    plt.imshow(img, aspect='auto')

    plt.savefig(self.output_filename)
    plt.show()
    plt.close()
