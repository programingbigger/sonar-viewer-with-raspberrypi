"""
描画の仕方(width x height)
- window
	- 800 x 900
	- 大枠のwindow

- canvas1
	- 800 x 600
	- 潜水艦ソナーの結果を描画

- canvas2
	- 800 x 300
	- 距離(cm)の結果を描画
	- 縦軸：距離
	- 横軸：時間-角度
"""


import tkinter as tk
from comp import hrc
from comp import servo
import RPi.GPIO as GPIO
import time
import math
import sys

# tkinterの初期化
root = tk.Tk()
root.geometry("800x900")
screen_name = root.winfo_screen()
print(f"Current screen: {screen_name}")
root.title("潜水艦ソナー")

# canvas1の設定
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH // 2 # 中心X
CENTER_Y = HEIGHT // 2 # 中心Y
RADIUS = min(CENTER_X, CENTER_Y) # 半径

# colorの設定
GREEN = "#00FF00"
RED = "#FF0000"

# canvas1（潜水艦風ソナーの設定）
WIDTH = 800
HEIGHT =  600
canvas1 = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas1.pack()

#  canvas2（距離の描画）
WIDTH_ = 800
HEIGHT_ =  300
canvas2 = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas2.pack()


def get_xy_sensor(agl):
		"""
		点座標の算出
		- 径に測定した距離から算出した割合をかける
		- HC-SR04の最大測定距離は450cmであることを考慮する
		"""
		servo.set_angle(angle = agl)
		distance = hrc.get_distance()
		radian = math.radians(agl) * (-1) # 補正
		x = CENTER_X + RADIUS * math.cos(radian) * (distance / 450)
		y = CENTER_Y + RADIUS * math.sin(radian) * (distance / 450)
		return x,y

try:
	# canvas1 setting
	# 半径RADIUS、中心CENTER_X、CENTER_Yの円を描画
	canvas1.create_oval(CENTER_X-RADIUS, CENTER_Y-RADIUS, CENTER_X+RADIUS, CENTER_Y+RADIUS, outline=GREEN)
	canvas1.create_line(CENTER_X-5, CENTER_Y-5, CENTER_X+5, CENTER_Y+5, width= 5, fill=RED)
	canvas1.create_line(CENTER_X-5, CENTER_Y+5, CENTER_X+5, CENTER_Y-5, width= 5, fill=RED)

	# 点を描画
	for i in range(0, 181, 1):
		X, Y = get_xy_sensor(agl = i)
		point = canvas1.create_oval(X - 2, Y - 2, X + 2, Y + 2, fill=GREEN, outline="")	
		root.update()
		time.sleep(0.2)

	for i in range(180, -1, -1):
		X, Y = get_xy_sensor(agl = i)
		point = canvas1.create_oval(X - 2, Y - 2, X + 2, Y + 2, fill=GREEN, outline="")
		root.update()
		time.sleep(0.2)

	# canvas2 setting
	canvas2.create_line(400, 0, 400, 300, width=10, fill=RED)

	root.mainloop()

except KeyboardInterrupt:
	# Ctrl + Cで処理を中断
	servo.stop_servo()
	GPIO.cleanup()
	sys.exit()
