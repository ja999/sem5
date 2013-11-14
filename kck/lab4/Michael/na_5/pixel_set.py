def white_neighbours(p):
  x, y = p
  points = []
  for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
      if (i != 0) or (j != 0):
        points.append((x + i, y + j))
  return points

def black_neighbours(p):
  x, y = p
  points = []
  for i in [-1, 1]:
    points.append((x + i, y))
    points.append((x, y + i))
  return points

def within_bounds(i, n):
  return (i >= 0) and (i < n)

class PixelSet:
  def __init__(self, img, img_sizes, x, y, vis):
    self.color = img[y][x]
    self.points = []
    self.edge_points = []
    self.img_sizes = img_sizes
    if self.color > 0:
      self.bfs(img, x, y, vis, white_neighbours)
      self.centroid = self.find_centroid()
    else:
      self.bfs(img, x, y, vis, black_neighbours)
      self.centroid = None

  def size(self):
    return len(self.points)

  def color(self):
    return self.color

  def bfs(self, img, i_x, i_y, vis, neighbour_function):
    queue = [(i_x, i_y)]
    vis[i_y][i_x] = True
    self.x_sizes = (i_x, i_x)
    self.y_sizes = (i_y, i_y)

    img_w, img_h = self.img_sizes

    while len(queue) > 0:
      point = queue.pop(0)
      self.points.append(point)
      new_points = neighbour_function(point)
      on_edge = False
      for p in new_points:
        x, y = p
        if within_bounds(x, img_w) and within_bounds(y, img_h):
          if self.color == img[y][x]:
            if not vis[y][x]:
              vis[y][x] = True
              self.x_sizes = (min(x, self.x_sizes[0]), max(x, self.x_sizes[1]))
              self.y_sizes = (min(y, self.y_sizes[0]), max(y, self.y_sizes[1]))
              queue.append(p)
          else:
            if not on_edge:
              on_edge = True
              self.edge_points.append(p)
    self.at_edge = (self.x_sizes[0] <= 0) or (self.x_sizes[1] >= img_w - 1) or (self.y_sizes[0] <= 0) or (self.y_sizes[1] >= img_h - 1)
    print 'color: %d, size: %d, at_edge: %d' % (self.color, len(self.points), self.at_edge)

  def find_centroid(self):
    xs = [p[0] for p in self.edge_points]
    ys = [p[1] for p in self.edge_points]
    l = len(self.edge_points)
    return (sum(xs) / l, sum(ys) / l)

  def bucket(self, img, color):
    for x, y in self.points:
      img[y][x] = color



