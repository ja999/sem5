#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

from matplotlib import colors
import colorsys

import math

def plot_color_gradients(gradients, names):
    # For pretty latex fonts
    # rc('text', usetex=True)
    # rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    return ( max(0, 2 * v - 1)
           , max(0, -2 * v + 1)
           , -abs(2 * v - 1) + 1
           )


def gradient_rgb_gbr_full(v):
    return ( min(1, max(0, 4 * v - 2))
           , min(1, max(0, -4 * v + 2))
           , min(1, -abs(4 * v - 2) + 2)
           )


def gradient_rgb_wb_custom(v):
    return ( min(1, max(0, -7 * v + 2, min(7 * v - 4, -7 * v + 7)))
           , min(1, max(0, -7 * v + 1, min(7 * v - 2, -7 * v + 6)))
           , min(1, max(0, -7 * v + 4))
           )


def gradient_hsv_bw(v):
    return colorsys.hsv_to_rgb(0, 0, v)


def gradient_hsv_bgr(v):
    return colorsys.hsv_to_rgb(0.333 + 0.667 * v, 1, 1)


def gradient_hsv_unknown(v):
    return colorsys.hsv_to_rgb(-0.32 * v + 0.32, 0.5, 0.9)


def gradient_hsv_custom(v):
    #return colorsys.hsv_to_rgb(math.sin(v), math.cos(v), max(0, min(1, math.cos(v) + math.sin(v) - abs(v - 0.5) + 0.2)))
    return colorsys.hsv_to_rgb(abs(math.sin(3 * v) + 0.3), abs(math.cos(1.57 * v)), 0.3 + 0.7 * math.sin(v * 1.57))


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_bgr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
