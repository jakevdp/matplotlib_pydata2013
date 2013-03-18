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


def button_press(event):
    c.xy_click = (event.x, event.y)
    if event.inaxes is ax:
        c.mouse_down = True

def button_release(event):
    c.mouse_down = False
    
def motion_notify(event):
    if c.mouse_down:
        dx = event.x - c.xy_click[0]
        dy = event.y - c.xy_click[1]
        c.xy_click = (event.x, event.y)
        c.rotate(c.y, -1E-2 * dx)
        c.rotate(c.x, 1E-2 * dy)
        fig.canvas.draw()
    
fig.canvas.mpl_connect('button_press_event', button_press)
fig.canvas.mpl_connect('button_release_event', button_release)
fig.canvas.mpl_connect('motion_notify_event', motion_notify)
