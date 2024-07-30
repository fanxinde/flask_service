作用：根据前端提供的 两个点，以及x和y的误差，以及数量，生成误差范围之内的点，返回一张图以及点的x，y值。

值得关注的点：
1、误差范围不填，则返回这条线上的点。
2、flask的模板，当第一次请求时返回默认值，之后每次请求会把上次请求的值返回到模板里面，而不是第一次请求的默认值，方便很多。

启动：
1、临时启动：/usr/local/bin/python3.9 /root/flask_service/app.py
2、后台启动：nohup python3.9 app.py   > app.log 2>&1 &

包：
flask
numpy
matplotlib

图例：
![image](https://github.com/user-attachments/assets/cfc64266-626e-4448-8184-4cd2b7e71409)
