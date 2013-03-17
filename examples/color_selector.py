"""
Interactive Matplotlib Color Selector

Written by Jake Vanderplas <jakevdp@cs.washington.edu>
"""


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, AxesWidget
from matplotlib.colors import rgb2hex

im_arr = np.zeros((256, 256, 3), dtype=np.float32)
im_arr[:, :, 0] = np.linspace(0, 1, 256)
im_arr[:, :, 1] = np.linspace(0, 1, 256)[:, np.newaxis]

fig = plt.figure(figsize=(8, 8))
main_ax = plt.axes([0.1, 0.15, 0.8, 0.8], xticks=[], yticks=[])
slider_ax = plt.axes([0.1, 0.1, 0.8, 0.02])
cbox_ax = plt.axes([0.1, 0.04, 0.04, 0.04], xticks=[], yticks=[])

slider = Slider(slider_ax, 'Blue', 0.0, 1.0, valinit=0.0, color='#AAAAFF')
im = main_ax.imshow(im_arr, extent=[0, 1, 0, 1], picker=True)

cbox_im = cbox_ax.imshow(np.ones((1, 1, 3)))
cbox_txt = cbox_ax.text(1.5, 0.5, "", transform=cbox_ax.transAxes,
                        fontsize=20, va='center', ha='left')

def update(val):
    im_arr[:, :, 2] = val
    im.set_data(im_arr)
    fig.canvas.draw()

def on_pick(event):
    r = event.mouseevent.xdata
    g = event.mouseevent.ydata
    b = slider.val
    cbox_im.set_data([[[r, 1 - g, b]]])
    cbox_txt.set_text(rgb2hex((r, g, b)).upper())
    fig.canvas.draw()
    

slider.on_changed(update)
fig.canvas.mpl_connect('pick_event', on_pick)

plt.show()
