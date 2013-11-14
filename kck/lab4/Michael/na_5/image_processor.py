from pixel_set import PixelSet
from skimage import morphology, filter, io
import matplotlib.pyplot as plt
from skimage.morphology import square

WHITE = 255
BLACK = 0

class ImageProcessor:
  def __init__(self, images):
    self.images = images

  def process_images(self):
    self.processed = []
    for img in self.images:
      self.processed.append(self.process_image(img))
    return self.processed

  def get_img_sizes(self, img):
    return (len(img[0]), len(img))

  def get_sets(self, img, img_sizes):
    w, h = img_sizes
    n = w * h
    vis = [x[:] for x in [[False]*w]*h]
    black_sets = []
    white_sets = []

    for j in range(0, h):
      if n <= 0:
        break
      for i in range(0, w):
        if (not vis[j][i]):
          new_set = PixelSet(img, img_sizes, i, j, vis)
          if new_set.color > 0:
            white_sets.append(new_set)
          else:
            black_sets.append(new_set)
          n -= new_set.size()
        if n <= 0:
          break
    return (black_sets, white_sets)

  def preprocess_image(self, img):
    img = filter.sobel(img)
    img = filter.canny(img, sigma=0.1, low_threshold=0.001, high_threshold=0.3)
    img = morphology.dilation(img, square(35))
    img = morphology.erosion(img, square(26))
    return img

  def process_image(self, img):
    img = self.preprocess_image(img)
    width, height = img_sizes = self.get_img_sizes(img)
    print img_sizes
    b, w = self.get_sets(img, img_sizes)

    print 'blacks: %d, whites: %d' % (len(b), len(w))

    for s in b:
      if not s.at_edge:
        s.bucket(img, WHITE)

    b, w = self.get_sets(img, img_sizes)
    avg_size = sum([s.size() for s in w]) / len(w)
    threshold = avg_size / 3
    out_w = []
    for s in w:
      if s.size() < threshold:
        s.bucket(img, BLACK)
      else:
        out_w.append(s)
    print len(b), len(w)
    return (img, [s.centroid for s in out_w])
