import matplotlib.pyplot as plt
from image_processor import ImageProcessor
from skimage import data, measure, io

def norm_cut(arg):
  return min(1, max(0, arg))

class Controller:
  def __init__(self, file_scheme, planes, output_file_scheme):
    self.output_file_scheme = output_file_scheme
    self.input_filenames = [file_scheme % plane for plane in planes]
    self.planes = planes
    self.files = []

  def parse_files(self):
    print 'parsing files...'
    for f in self.input_filenames:
      self.files.append((data.imread(f), data.imread(f, as_grey = True)))
    print '...done'

  def process_files(self):
    print 'processing files...'
    img_p = ImageProcessor([f[1] for f in self.files])
    self.processed = img_p.process_images()
    print '...done'

  def plot_files(self):
    print 'drawing images...'
    for i, f in enumerate(self.files):
      print '...drawing #%02d: %02d' % (i, self.planes[i])
      fig = plt.figure()
      fig.add_axes([-0.15, -0.075, 1.2, 1.2])
      io.imshow(f[0])
      contours = measure.find_contours(self.processed[i][0], 0.9)
      for n, contour in enumerate(contours):
        plt.plot(contour[:, 1], contour[:, 0], linewidth = 3)
      centroids = self.processed[i][1]
      c_x = [c[0] for c in centroids]
      c_y = [c[1] for c in centroids]
      plt.scatter(c_x, c_y, color = 'white')
      plt.xticks([])
      plt.yticks([])
      plt.savefig(self.output_file_scheme % self.planes[i])
      plt.close()
    print '...done'
