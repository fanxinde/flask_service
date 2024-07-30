import numpy as np
import matplotlib.pyplot as plt

def generate_random_points_on_line(x1, y1, x2, y2, num_points):
    # 计算直线的斜率
    slope = (y2 - y1) / (x2 - x1)
    # 生成num_points个随机x坐标，在x1和x2之间
    x_random = np.random.uniform(x1, x2, num_points)
    # 计算对应的y坐标
    y_random = slope * (x_random - x1) + y1
    return x_random, y_random

# 示例点
x1, y1 = 3, 144.3
x2, y2 = 600, 119.9

# 生成10个随机点
num_points = 100
x_random, y_random = generate_random_points_on_line(x1, y1, x2, y2, num_points)

# 可视化
plt.plot([x1, x2], [y1, y2], label='Line')
plt.scatter(x_random, y_random, color='red', label='Random Points')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Random Points on a Line')
plt.show()
