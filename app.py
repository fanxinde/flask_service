from flask import Flask, request, jsonify, render_template
import random
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def generate_random_points_with_xy_error(x1, y1, x2, y2, num_points, x_error_range, y_error_range):
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


def generate_points(start_x, start_y, end_x, end_y, error_range_x, error_range_y, num_points):
    # 示例点
    # x1, y1 = 3, 144.3
    # x2, y2 = 600, 119.9
    points = []

    # 生成10个带误差的随机点
    # num_points = 50
    # x_error_range = 0.2  # x坐标误差范围
    # y_error_range = 0.2  # y坐标误差范围
    x_random_with_error, y_random_with_error = generate_random_points_with_xy_error(start_x, start_y, end_x, end_y, num_points, error_range_x, error_range_y)

    # 打印生成的点
    print("Generated points with XY-error:")
    for x, y in zip(x_random_with_error, y_random_with_error):
        points.append((x, y))
        print(f"({x:.2f}, {y:.2f})")


    return points, True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_x = float(request.form['start_x'])
        start_y = float(request.form['start_y'])
        end_x = float(request.form['end_x'])
        end_y = float(request.form['end_y'])

        error_range_x = request.form.get('error_range_x')
        error_range_y = request.form.get('error_range_y')
        num_points = int(request.form.get('num_points', 50))

        # Convert error ranges to float if they are provided, otherwise None
        error_range_x = float(error_range_x) if error_range_x else 0
        error_range_y = float(error_range_y) if error_range_y else 0

        points, success = generate_points(start_x, start_y, end_x, end_y, error_range_x, error_range_y, num_points)

        if not success:
            return render_template('index.html',
                                   error="Error: Unable to generate the requested number of points. Adjust the error ranges or point limits.")

        x_values = [point[0] for point in points]
        y_values = [point[1] for point in points]

        plt.figure(figsize=(8, 6))
        plt.scatter(x_values, y_values, color='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Scatter Plot of Generated Points')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()

        # Convert plot to base64 string
        img_data = BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        img_base64 = base64.b64encode(img_data.getvalue()).decode()
        plt.close()

        # 准备要传递给模板的数据
        info = {
            'img_base64': img_base64,
            'points': points,
            'start_x': start_x,
            'start_y': start_y,
            'end_x': end_x,
            'end_y': end_y,
            'error_range_x': error_range_x,
            'error_range_y': error_range_y,
            'num_points': num_points
        }
        points.sort(key=lambda point: point[0])
        return render_template('index.html', info=info, points=points,
                               start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y,
                               error_range_x=error_range_x, error_range_y=error_range_y, num_points=num_points)

    return render_template('index.html',
                           start_x='-5', start_y='-5', end_x='5', end_y='5',
                           error_range_x='', error_range_y='', num_points=50)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
