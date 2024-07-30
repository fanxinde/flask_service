from flask import Flask, request, jsonify, render_template
import random
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def generate_points(a, b, c, start_x, start_y, end_x, end_y, error_range_x, error_range_y, num_points):
    points = []
    step = 0.1  # 步长，可以根据需要调整
    count = 0

    while count < num_points:
        x = random.uniform(start_x, end_x)
        y_actual = a * x**2 + b * x + c

        # 在实际值附近加入一定的误差
        x_generated = x + random.uniform(-error_range_x, error_range_x)
        y_generated = y_actual + random.uniform(-error_range_y, error_range_y)

        # 确保生成的点在范围内
        if start_x <= x_generated <= end_x and start_y <= y_generated <= end_y:
            points.append((x_generated, y_generated))
            count += 1
    print(points)
    return points

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])
        start_x = float(request.form['start_x'])
        start_y = float(request.form['start_y'])
        end_x = float(request.form['end_x'])
        end_y = float(request.form['end_y'])
        error_range_x = float(request.form['error_range_x'])
        error_range_y = float(request.form['error_range_y'])
        num_points = int(request.form['num_points'])

        points = generate_points(a, b, c, start_x, start_y, end_x, end_y, error_range_x, error_range_y, num_points)

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
	        'a': a,
            'b': b,
            'c': c,
            'start_x': start_x,
            'start_y': start_y,
            'end_x': end_x,
            'end_y': end_y,
            'error_range_x': error_range_x,
            'error_range_y': error_range_y,
            'num_points': num_points
        }
        points.sort(key=lambda point: point[0])
        return render_template('index.html', info=info, points=points)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


