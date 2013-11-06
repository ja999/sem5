def avg(arr):
  return sum(arr) / len(arr)

class MapPoint:
  def __init__(self, value):
    self.value = value
    self.normal = None
    self.line_top = None
    self.line_bottom = None
    self.line_left = None
    self.line_right = None

  def calculate_normal(self):
    if self.normal is None:
      verticals = []
      for l in [self.line_top, self.line_bottom]:
        if l:
          verticals.append(l.normal)
      horizontals = []
      for l in [self.line_left, self.line_right]:
        if l:
          horizontals.append(l.normal)
      if len(horizontals) > 0 and len(verticals) > 0:
        hor = (avg([v[0] for v in horizontals]), avg([v[1] for v in horizontals]), 0)
        ver = (0, avg([v[1] for v in horizontals]), avg([v[0] for v in horizontals]))
        self.normal = [avg([hor[i], ver[i]]) for i in range(0, 3)]
