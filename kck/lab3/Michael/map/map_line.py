def normal_length(x, y):
  return (x ** 2 + y ** 2) ** 0.5

class MapLine:
  def __init__(self, first_point, second_point, unit):
    self.first = first_point
    self.second = second_point
    self.unit = unit

    dh = first_point.value - second_point.value
    length = normal_length(dh, unit)
    self.normal = (dh / length, unit / length)

