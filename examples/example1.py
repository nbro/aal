import matplotlib as mpl

mpl.use('Qt5Agg')

import matplotlib.pyplot as plt
import numpy as np
from shapely import affinity
from shapely.geometry import LineString
from similaritymeasures import dtw, frechet_dist

from aal import d_warp, to_aal


def rotate(a, angle):
    return list(affinity.rotate(LineString(a), angle, 'center').coords)


def main():
    a = [(0.39, 0.8), (0.3, 0.45), (0.35, 0.78), (0.4, 0.3), (0.49, 0.8),
         (0.51, 0.23), (0.6, 0.71)]

    dtws_xy = []
    dtws_aal = []
    frechets_xy = []
    frechets_aal = []

    angles = range(0, 360, 30)

    for i, angle in enumerate(angles):
        b = rotate(a, angle)

        dtw_xy, d_xy = dtw(a, b)
        dtws_xy.append(dtw_xy)

        fd_xy = frechet_dist(a, b)
        frechets_xy.append(fd_xy)

        # Convert the trajectories a and b to the trajectories in the AAL
        # space.
        aal_a, aal_b = to_aal([a, b])

        dtw_aal, d_aal = dtw(aal_a, aal_b, metric=d_warp)
        dtws_aal.append(dtw_aal)

        fd_aal = frechet_dist(aal_a, aal_b)
        frechets_aal.append(fd_aal)

        a_angles, a_arc_lengths = zip(*aal_a)
        b_angles, b_arc_lengths = zip(*aal_b)

        f1 = plt.figure(1)
        plt.subplot(4, 3, i + 1)
        plt.plot(a_arc_lengths, a_angles, label="T")
        plt.plot(b_arc_lengths, b_angles, label="Q")
        plt.legend(prop={'size': 6})
        plt.xlabel("Arc-length", fontsize=8)
        plt.ylabel("Angle", fontsize=8)
        plt.xticks(np.linspace(0, 1, num=5), np.linspace(0, 1, num=5),
                   fontsize=8)
        plt.yticks([-np.pi, 0, np.pi], labels=[u"-\u03C0", "0", "\u03C0"],
                   fontsize=8)
        plt.title("Angle={0:.1f} (rad)".format(np.radians(angle)), fontsize=8)
        f1.tight_layout()

        a_xs, a_ys = zip(*a)
        b_xs, b_ys = zip(*b)

        plt.figure(2)
        plt.subplot(4, 3, i + 1, aspect='equal', adjustable='box')
        plt.plot(a_xs, a_ys, label="T")
        plt.plot(b_xs, b_ys, label="Q")
        plt.xlabel("x", fontsize=8)
        plt.ylabel("y", fontsize=8)
        plt.title("Angle={0:.1f} (rad)".format(np.radians(angle)), fontsize=8)
        plt.xticks(np.linspace(0, 1, num=3), np.linspace(0, 1, num=3),
                   fontsize=8)
        plt.yticks(np.linspace(0, 1, num=5), np.linspace(0, 1, num=5),
                   fontsize=8)

    plt.tight_layout()

    angles = [np.radians(x) for x in angles]
    plt.figure(3)
    plt.plot(angles, dtws_xy, label="DTW")
    plt.plot(angles, frechets_xy, label="Frechet")
    plt.title("XY space")
    plt.xlabel("Rotation Angle")
    plt.ylabel("Distances")
    plt.legend(prop={'size': 6})

    plt.figure(4)
    plt.plot(angles, dtws_aal, label="DTW")
    plt.plot(angles, frechets_aal, label="Frechet")
    plt.title("AAL space")
    plt.xlabel("Rotation Angle")
    plt.ylabel("Distances")
    plt.legend(prop={'size': 6})

    plt.show()


if __name__ == '__main__':
    plt.close('all')
    main()
