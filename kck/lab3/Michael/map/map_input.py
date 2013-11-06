class MapInput:
  def __init__(self, file_name):
    self.file_name = file_name
    self.rows = None
    self.matrix = None
    self.cols = None
    self.unit = None

  def parse(self):
    self.matrix = []
    with open(self.file_name, "rb") as f:
      text = f.read().split('\n')
      self.rows, self.cols, self.unit = [int(x) for x in text[0].strip().split(' ')]
      self.unit = float(self.unit) / 100

      for line in text[1:]:
        l = line.strip()
        if l:
          new_line = []
          self.matrix.append(new_line)
          for h in l.strip().split(' '):
            new_line.append(float(h))
    return (self.matrix, self.rows, self.cols, self.unit)



