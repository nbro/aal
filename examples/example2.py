import matplotlib as mpl

mpl.use('Qt5Agg')

import matplotlib.pyplot as plt
import numpy as np
from similaritymeasures import dtw, frechet_dist

from aal import d_warp, to_aal


def generate_sine_coords(num=100):
    return [(x, np.sin(x) * 10) for x in range(num)]


def main():
    a = generate_sine_coords(7)

    dtws_xy = []
    dtws_aal = []
    frechets_xy = []
    frechets_aal = []

    num_points = range(14, 7 * 20, 7)

    for num in num_points:
        b = generate_sine_coords(num)

        dtw_xy, d_xy = dtw(a, b)
        dtws_xy.append(dtw_xy)

        fd_xy = frechet_dist(a, b)
        frechets_xy.append(fd_xy)

        # Convert the two curves, a and b, to the AAL space.
        a_aal, b_aal = to_aal([a, b])

        dtw_aal, d_aal = dtw(a_aal, b_aal, metric=d_warp)
        dtws_aal.append(dtw_aal)

        fd_aal = frechet_dist(a_aal, b_aal)
        frechets_aal.append(fd_aal)

        a_angles, a_arc_lengths = zip(*a_aal)
        b_angles, b_arc_lengths = zip(*b_aal)

        plt.figure(1)
        plt.plot(a_arc_lengths, a_angles, label="a")
        plt.plot(b_arc_lengths, b_angles, label="b")
        plt.xlabel("Arc-length", fontsize=8)
        plt.ylabel("Angle", fontsize=8)
        plt.title("AAL Space", fontsize=8)

        a_xs, a_ys = zip(*a)
        b_xs, b_ys = zip(*b)

        plt.figure(2)
        plt.plot(a_xs, a_ys, label="a")
        plt.plot(b_xs, b_ys, label="b")
        plt.xlabel("z", fontsize=8)
        plt.ylabel("y", fontsize=8)
        plt.title("XY Space", fontsize=8)

    num_points = list(num_points)

    plt.figure(3)
    plt.plot(num_points, dtws_xy, label="DTW")
    plt.plot(num_points, frechets_xy, label="Frechet")
    plt.xlabel("Number of nodes")
    plt.ylabel("Distance")
    plt.title("XY space")

    plt.figure(4)
    plt.plot(num_points, dtws_aal, label="DTW")
    plt.plot(num_points, frechets_aal, label="Frechet")
    plt.xlabel("Number of nodes")
    plt.ylabel("Distance")
    plt.title("AAL space")

    plt.show()


if __name__ == '__main__':
    plt.close('all')
    main()
