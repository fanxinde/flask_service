import numpy as np
import matplotlib.pyplot as plt

def generate_random_points_with_xy_error(x1, y1, x2, y2, num_points, x_error_range=0, y_error_range=0):
    # 计算直线的斜率
    slope = (y2 - y1) / (x2 - x1)
    # 生成num_points个随机x坐标，在x1和x2之间
    x_random = np.random.uniform(x1, x2, num_points)
    # 添加随机误差到x坐标
    x_random_with_error = x_random + np.random.uniform(-x_error_range, x_error_range, num_points)
    # 计算对应的y坐标
    y_random = slope * (x_random_with_error - x1) + y1
    # 添加随机误差到y坐标
    y_random_with_error = y_random + np.random.uniform(-y_error_range, y_error_range, num_points)
    return x_random_with_error, y_random_with_error

# 示例点
x1, y1 = 3, 144.3
x2, y2 = 600, 119.9

# 生成10个带误差的随机点
num_points = 500
x_error_range = 0.2  # x坐标误差范围
y_error_range = 0.2  # y坐标误差范围
x_random_with_error, y_random_with_error = generate_random_points_with_xy_error(x1, y1, x2, y2, num_points, x_error_range, y_error_range)

# 打印生成的点
print("Generated points with XY-error:")
for x, y in zip(x_random_with_error, y_random_with_error):
    print(f"({x:.2f}, {y:.2f})")

# 可视化
plt.plot([x1, x2], [y1, y2], label='Line')
plt.scatter(x_random_with_error, y_random_with_error, color='red', label='Random Points with XY Error')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Random Points on a Line with XY Error')
plt.show()
