from map_point import MapPoint
from map_line import MapLine

def dot_product(v1, v2):
  return sum([a * b for a, b, in zip(v1, v2)])

def vector_length(v):
  return sum([x ** 2 for x in v]) ** 0.5

def vector_cosine(v1, v2):
  return dot_product(v1, v2) / (vector_length(v1) * vector_length(v2))

class ColorfulMap:
  def __init__(self, sun_vector):
    self.matrix = []
    self.sun_vector = sun_vector

  def load(self, matrix, rows, cols, unit):
    self.rows = rows
    self.cols = cols
    self.unit = unit
    if rows > 0 and cols > 0:
      self.min_value = matrix[0][0]
      self.max_value = matrix[0][0]
      for row_i in matrix:
        new_row = []
        self.matrix.append(new_row)
        for h_ij in row_i:
          new_row.append(MapPoint(h_ij))
          self.min_value = min(self.min_value, h_ij)
          self.max_value = max(self.max_value, h_ij)

        for j in range(0, cols - 1):
          new_line_h = MapLine(new_row[j], new_row[j + 1], unit)
          new_row[j].line_right = new_line_h
          new_row[j + 1].line_left = new_line_h

      for j in range(0, cols):
        for i in range(0, rows - 1):
          new_line_v = MapLine(self.matrix[i][j], self.matrix[i + 1][j], unit)
          self.matrix[i][j].line_bottom = new_line_v
          self.matrix[i + 1][j].line_top = new_line_v

      self.d_value = self.max_value - self.min_value
    return self

  def color(self, i, j):
    point = self.matrix[i][j]
    point.calculate_normal()

    return (self.normalize_value(point.value), vector_cosine(self.sun_vector, point.normal))

  def normalize_value(self, value):
    return (value - self.min_value) / self.d_value


