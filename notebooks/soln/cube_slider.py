from tutorial_lib.simple_cube import Cube
c = Cube()
fig, ax = plt.subplots(figsize=(8, 8),
                       subplot_kw=dict(xticks=[], yticks=[]))
c.add_to_ax(ax)
c.rotate(c.x - c.y, -np.pi / 6)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)


def zoom(val):
    c.set_view((0, 0, val))
    ax.set_xlim(-val, val)
    ax.set_ylim(-val, val)
    fig.canvas.draw()
    
slider_ax = fig.add_axes((0.2, 0.05, 0.6, 0.02))
slider = Slider(slider_ax, "perspective", 1, 20, valinit=10, color='#AAAAAA')
slider.on_changed(zoom)
