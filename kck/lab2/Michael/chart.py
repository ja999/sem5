from chart_point import ChartPoint
import csv
import os 

class Chart:
  def __init__(self, filename):
    self.points = []
    self._min = -1
    self._max = -1
    self.filename = filename
    self.curve_name = os.path.basename(filename).replace(".csv", "", 1)
    self.parse_file(filename)
    if len(self.points) > 0:
      self.set_plot_attributes()

  def parse_file(self, filename):
    with open(filename, "rb") as csvfile:
      file_reader = csv.reader(csvfile, delimiter = ",")
      for row in file_reader:
        self.add_point(row)

  def get_plot_args(self):
    return [self.left_bottom_x, self.left_y]

  def add_point(self, row):
    try:
      point = ChartPoint(row)
      self.points.append(point)
      self.set_min_max(len(self.points) - 1)
      return point
    except Exception as e:
      return e

  def set_min_max(self, idx):
    point = self.points[idx]
    if self._min == -1:
      self._min = idx
      self._max = idx
    else:
      if point.avg < self.points[self._min].avg:
        self._min = idx
      elif point.avg > self.points[self._max].avg:
        self._max = idx

  def set_plot_attributes(self):
    first_point = self.first_point()
    last_point = self.last_point()
    self.left_y = [x.avg * 100 for x in self.points]
    self.left_bottom_x = [float(x.games) / 1000 for x in self.points]
    self.box = [x * 100 for x in last_point.points]
    self.box_medium = last_point.avg * 100

    self.min_low_x = float(first_point.games) / 1000
    self.max_low_x = float(last_point.games) / 1000
    self.min_top_x = float(first_point.generation)
    self.max_top_x = float(last_point.generation)
    self.min_y = self.points[self._min].avg * 100
    self.max_y = self.points[self._max].avg * 100

  def first_point(self):
    return self.points[0]

  def last_point(self):
    return self.points[-1]

