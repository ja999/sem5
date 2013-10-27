import matplotlib.pyplot as plt
import glob
import math
from chart import Chart

class Controller:
  ER_NO_CHARTS = "There're no charts loaded to print them!"
  def __init__(self, dir, output_filename):
    self.dir = dir
    self.output_filename = output_filename
    self.charts = []
    self.files = glob.glob(dir + "/*.csv")

  def parse_files(self):
    self.charts = []
    for f in self.files:
      self.charts.append(Chart(f))
    self.charts = sorted(self.charts, key = lambda(chart): -chart.box_medium)

  def plot(self, low_xlabel, top_xlabel, ylabel, markers, colors, label_rotation = 20, loc = 4, alpha = 0.75, legend_size = 12, figsize = (10, 6.7)):
    fig = plt.figure(figsize = figsize)
    if len(self.charts) <= 0:
      print(Controller.ER_NO_CHARTS)
    else:
      plt.rcParams['font.family'] = 'Times New Roman'
      self.set_plot_attributes(markers, colors)
      self.plot_curves(plt, fig, low_xlabel, top_xlabel, ylabel, loc, alpha, legend_size)
      self.plot_boxes(plt, fig, label_rotation = label_rotation)

    plt.savefig(self.output_filename)
    plt.close()

  def set_plot_attributes(self, markers, colors):
    self.left_low_x_min = min([c.min_low_x for c in self.charts])
    self.left_low_x_max = max([c.max_low_x for c in self.charts])
    self.left_low_fragment = int(floor_fragment(tick_every(self.left_low_x_min, self.left_low_x_max, 5), 100))
    self.left_low_x_min = floor_fragment(self.left_low_x_min, self.left_low_fragment)
    self.left_low_x_max = floor_fragment(self.left_low_x_max, self.left_low_fragment)

    self.left_top_x_min = min([c.min_top_x for c in self.charts])
    self.left_top_x_max = max([c.max_top_x for c in self.charts]) + 1
    self.left_top_fragment = tick_every(self.left_top_x_min, self.left_top_x_max, 5)
    self.left_markevery = tick_every(self.left_top_x_min, self.left_top_x_max, 9)

    self.y_min = floor_fragment(self.charts[-1].min_y, 5)
    self.y_max = ceil_fragment(self.charts[0].max_y, 5)

    self.markers = markers
    self.len_markers = len(self.markers)
    self.colors = colors
    self.len_colors = len(self.colors)

  def plot_curves(self, plt, fig, low_xlabel, top_xlabel, ylabel, loc, alpha, legend_size):
    ax_low = fig.add_subplot(121)
    ax_top = ax_low.twiny()
    ax_low.set_xlim([self.left_low_x_min, self.left_low_x_max])
    ax_low.set_xticks(range(int(self.left_low_x_min), int(self.left_low_x_max) + 1, self.left_low_fragment))
    ax_low.set_ylim([self.y_min, self.y_max])
    ax_top.set_xlim([self.left_top_x_min, self.left_top_x_max])
    ax_top.set_xticks(range(int(self.left_top_x_min), int(self.left_top_x_max) + 1, self.left_top_fragment))
    for i, c in enumerate(self.charts):
      line = ax_low.plot(*c.get_plot_args(), label = c.curve_name, marker = self.markers[i % self.len_markers], color = self.colors[i % self.len_colors])
      line[0].set_markevery(self.left_markevery)
    legend = ax_low.legend(loc = loc, fancybox = True, prop = { 'size': legend_size })
    legend.get_frame().set_alpha(alpha)
    ax_low.grid()
    ax_low.set_xlabel(low_xlabel)
    ax_top.set_xlabel(top_xlabel)
    ax_low.set_ylabel(ylabel)

  def plot_boxes(self, plt, fig, label_rotation):
    boxes_range_max = len(self.charts) + 1
    boxes_range = range(1, boxes_range_max)

    ax = fig.add_subplot(122)
    plt.xticks(boxes_range, [c.curve_name for c in self.charts], rotation = label_rotation)
    ax.yaxis.tick_right()
    ax.grid()
    ax.set_ylim([self.y_min, self.y_max])
    ax.set_xlim([0, boxes_range_max])

    ax.boxplot(self.get_boxes(), 1)
    ax.scatter(boxes_range, self.get_avgs_for_boxes())

  def get_boxes(self):
    return [c.box for c in self.charts]

  def get_avgs_for_boxes(self):
    return [c.points[-1].avg * 100 for c in self.charts]

def ceil_fragment(arg, frag = 1):
  frag = int(frag)
  return math.ceil(float(arg / frag)) * frag

def floor_fragment(arg, frag = 1):
  frag = int(frag)
  return math.floor(float(arg / frag)) * frag

def tick_every(axis_min, axis_max, markers):
  return int(math.ceil((axis_max - axis_min) / markers))

