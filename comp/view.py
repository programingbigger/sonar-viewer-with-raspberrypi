import tkinter as tk
from hrc import get_distance
from servo import set_angle
from servo import stop_servo
import time
import math

# ウィンドウの設定
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = min(CENTER_X, CENTER_Y) * 0.9 # 半径の設定

# 残像の設定
FADE_TIME = 5  # second

# tkinterの初期化
root = tk.Tk()
root.title("潜水艦ソナー")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# アプリケーションの実行
root.mainloop()

"""
　残像をフェードアウト
"""
def fade_point(point):
    alpha = 1.0
    for i in range(100):
        after_id = canvas.after(int(FADE_TIME * 10), lambda a=alpha: canvas.itemconfig(point, fill="", outline=""))
        alpha -= 0.01
        canvas.after_cancel(after_id)
    canvas.after(int(FADE_TIME * 1000), lambda: canvas.delete(point))

def calculate_color(distance):
    """距離に応じて色を計算する"""
    # 距離が近いほど緑、遠いほど赤
    green_value = int(max(0, 255 - distance * 2))
    red_value = int(min(255, distance * 2))
    return f"#{red_value:02X}{green_value:02X}00"

def update_sonar():
    """ソナーを更新する"""
    angle = 0  # サーボモータの開始角度
    while angle < 21:
        set_angle(angle)
        distance = get_distance()

        # 距離に応じた色を算出
        color = calculate_color(distance)

        # 点座標の算出
        radian = math.radians(angle)
        x = CENTER_X + RADIUS * math.cos(radian) * (distance / 100)
        y = CENTER_Y + RADIUS * math.sin(radian) * (distance / 100)

        # 点を描画
        point = canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill=color, outline="")

        # 残像をフェードアウト
        fade_point(point)

        # サーボの角度を更新
        angle += 1

        # 描画を更新
        root.update()

    # サーボを初期位置に戻す
    set_servo_angle(0)

# ソナーを更新
while True:
    update_sonar()
