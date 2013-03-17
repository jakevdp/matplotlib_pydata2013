import numpy as np
import matplotlib.pyplot as plt
from projection import Quaternion, project_points


class Cube(object):
    """An Axes for displaying a 3D cube"""
    # fiducial face is perpendicular to z at z=+1
    one_face = np.array([[1, 1, 1], [1, -1, 1], [-1, -1, 1],
                         [-1, 1, 1], [1, 1, 1]])

    # Construct six rotators for the cube faces. These will take a single
    # fiducial face, and rotate it to the appropriate 3D location.
    x, y, z = np.eye(3)
    _rots = [Quaternion.from_v_theta(x, theta)
             for theta in (np.pi / 2, -np.pi / 2)]
    _rots += [Quaternion.from_v_theta(y, theta)
              for theta in (np.pi / 2, -np.pi / 2, np.pi, 2 * np.pi)]
    _faces = np.array([np.dot(one_face, rot.as_rotation_matrix().T)
                       for rot in _rots])

    def __init__(self, view=(0, 0, 10), colors=None, alpha=0.8):
        self.view = view
        self.current_rotation = Quaternion.from_v_theta((0, 0, 1), 0)

        if colors is None:
            colors = ['blue', 'green', 'white', 'yellow', 'orange', 'red']
        else:
            assert len(colors) == 6

        self.polys = [plt.Polygon(self._faces[i, :, :2],
                                  facecolor=colors[i],
                                  alpha=alpha)
                      for i in range(6)]

    def rotate(self, v, theta):
        new_rot = Quaternion.from_v_theta(v, theta)
        self.current_rotation = self.current_rotation * new_rot
        
        faces_proj = project_points(self._faces, self.current_rotation,
                                    self.view)
        xy = faces_proj[:, :, :2]
        zorder = -faces_proj[:, :4, 2].mean(-1)

        for i in range(6):
            self.polys[i].set_xy(xy[i])
            self.polys[i].set_zorder(zorder[i])

    def set_view(self, view):
        self.view = view
        self.rotate(self.z, 0)

    def add_to_ax(self, ax):
        for poly in self.polys:
            ax.add_patch(poly)
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(6, 6),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    c = Cube()
    c.add_to_ax(ax)

    c.rotate((1, -1, 0), -np.pi / 6)

    plt.show()
