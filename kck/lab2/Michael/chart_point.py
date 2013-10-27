def avg(arr):
  return sum(arr) / float(len(arr))

def median(arr):
  l = len(arr)
  hl = int(l / 2)
  if l % 2 == 1:
    return arr[hl]
  return arr[hl] + arr[hl + 1]

class ChartPoint:
  def __init__(self, row):
    self.generation = int(row[0])
    self.games = int(row[1])
    self.points = sorted([float(x) for x in row[2:]])
    self.avg = avg(self.points)
    self.median = median(self.points)

