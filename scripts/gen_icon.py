import math
import matplotlib.pyplot as plt
import numpy as np

from spiral_calc import rotate_points, generate_logarithmic_spiral_points


def simulate_milky_way_arms():
    # 生成原始螺旋线
    points = generate_logarithmic_spiral_points(a=0.1, b=0.2, num_points=500, end_angle=2 * math.pi)

    points1 = rotate_points(points, math.pi * 30 / 180)
    points2 = rotate_points(points, math.pi * 120 / 180)
    points3 = rotate_points(points, math.pi * 210 / 180)
    points4 = rotate_points(points, math.pi * 300 / 180)

    # 绘制四条螺旋线
    x1, y1 = zip(*points1)
    x2, y2 = zip(*points2)
    x3, y3 = zip(*points3)
    x4, y4 = zip(*points4)

    plt.plot(x1, y1, label="Spiral 1 (Perseus Arm)")
    plt.plot(x2, y2, label="Spiral 2 ()")
    plt.plot(x3, y3, label="Spiral 3 (Scutum-Centaurus Arm)")
    plt.plot(x4, y4, label="Spiral 4 ()")

    plt.axis('equal')
    plt.legend()
    plt.title("Four Symmetric Logarithmic Spirals (Rotation)")
    plt.show()


if __name__ == '__main__':
    simulate_milky_way_arms()
