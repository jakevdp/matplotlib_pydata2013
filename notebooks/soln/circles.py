N = 30
fig, ax = plt.subplots()
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(-0.3, 1.3)

for i in range(N):
    circ = plt.Circle(np.random.random(2), 0.1 * (1 + np.random.random()),
                      alpha=0.5, picker=True)
    ax.add_patch(circ)

def on_pick(event):
    artist = event.artist
    artist.set_color(np.random.random(3))
    fig.canvas.draw()
    
fig.canvas.mpl_connect('pick_event', on_pick)
