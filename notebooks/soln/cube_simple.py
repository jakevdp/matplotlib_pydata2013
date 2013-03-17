fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(xticks=[], yticks=[]))
c = Cube()
c.rotate(c.x - c.y, -np.pi / 6)
c.add_to_ax(ax)

def button_press(event):
    c.xy_click = (event.x, event.y)
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
