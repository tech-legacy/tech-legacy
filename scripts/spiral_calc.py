import math
import matplotlib.pyplot as plt
import numpy as np


def rotate_points(points, angle):
    """
    将点列表旋转指定角度（弧度）。

    参数：
        points (list): 包含 (x, y) 坐标的列表。每个元组 (x, y) 代表螺旋线上的一个点。

        angle (float): 旋转角度（弧度）。
            - 旋转 90 度 = math.pi * 90 / 180
            - 旋转 180 度 = math.pi
            - 旋转 270 度 = math.pi * 270 / 180
    """
    rotated_points = []
    for x, y in points:
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)
        rotated_points.append((new_x, new_y))
    return rotated_points


def generate_logarithmic_spiral_points(a=0.1,
                                       b=0.2,
                                       num_points=1000,
                                       start_angle=0,
                                       end_angle=20 * math.pi):
    """
    生成对数螺旋的坐标点。

    对数螺旋的极坐标方程为：r = a * exp(b * theta)

    参数：
        a (float): 对数螺旋公式中的参数 a。控制螺旋的起始半径（theta=0 时的半径）。
            数据范围：a > 0。如果 a <= 0，函数将打印错误信息并返回空列表。
            较小的 a 值会使螺旋更靠近原点开始。

        b (float): 对数螺旋公式中的参数 b。控制螺旋的增长速度。
            数据范围：b 可以是任意实数。
            如果 b > 0，螺旋向外扩展（逆时针）。
            如果 b < 0，螺旋向内收缩（顺时针）。
            b 的绝对值越大，螺旋增长/收缩的速度越快。

        num_points (int): 生成的点数。决定了螺旋曲线的平滑度。
            数据范围：num_points > 0。如果 num_points <= 0，函数将打印错误信息并返回空列表。
            较大的 num_points 值会生成更平滑的曲线，但也需要更多的计算资源。

        start_angle (float): 起始角度（弧度）。
            数据范围：可以是任意实数。通常用于控制螺旋的起始位置。

        end_angle (float): 结束角度（弧度）。
            数据范围：可以是任意实数，但必须大于 start_angle。
            如果 end_angle <= start_angle，函数将打印错误信息并返回空列表。
            end_angle - start_angle 的差值决定了螺旋的圈数。例如，end_angle - start_angle = 2*pi 表示一圈。

    返回：
        list: 包含 (x, y) 坐标的列表。每个元组 (x, y) 代表螺旋线上的一个点。
            如果输入参数不合法，则返回一个空列表。
    """

    if num_points <= 0 or start_angle >= end_angle or a <= 0:
        print("参数不合法：num_points 必须大于 0，start_angle 必须小于 end_angle，a必须大于0。")
        return []

    points = []
    angle_step = (end_angle - start_angle) / (num_points - 1) if num_points > 1 else 0

    for i in range(num_points):
        theta = start_angle + i * angle_step
        r = a * math.exp(b * theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((x, y))

    return points


def generate_logarithmic_spiral_points_v2(a, b, theta_start, theta_end, num_points):
    """
    Generate points for a logarithmic spiral based on its polar equation.

    Parameters:
        a (float): The initial radius at theta = 0.
        b (float): The growth rate of the spiral.
        theta_start (float): The starting angle (in radians).
        theta_end (float): The ending angle (in radians).
        num_points (int): The number of points to generate.

    Returns:
        tuple: Two numpy arrays, one for x coordinates and one for y coordinates.
    """
    # Generate theta values
    theta = np.linspace(theta_start, theta_end, num_points)

    # Calculate the radius for each theta
    r = a * np.exp(b * theta)

    # Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    points = np.column_stack((x, y))
    return points


if __name__ == '__main__':
    """
    示例：
        生成一个从 0 度到 2π 弧度的螺旋线，并绘制出来：
    """
    points = generate_logarithmic_spiral_points(a=0.1, b=0.2, num_points=500, start_angle=0, end_angle=2 * math.pi)
    x, y = zip(*points)
    plt.plot(x, y, label="Gemini")

    # 对比
    points2 = generate_logarithmic_spiral_points_v2(a=0.1, b=0.2, theta_start=0, theta_end=2 * np.pi, num_points=500)
    points2 = rotate_points(points2, math.pi)
    x2, y2 = zip(*points2)
    plt.plot(x2, y2, label="ChatGPT")

    plt.axis('equal')
    plt.show()
