"""
- アーキテクチャ
	- 1：サーボ⇨0°
	- 2：測定
	- 3：コマンドプロンプトに表示
"""
from hrc import get_distance
from servo import set_angle
from servo import stop_servo
import time

def format_(agl:int, dis:int) -> str:
	print(f"{agl} degree")
	print(f"{dis:.3f}")

try:
	n = 90 # degree
	
	for i in range(0, n+1, 1):
		set_angle(i)
		dis = get_distance()
		format_(i, dis)
		time.sleep(0.1)
	
	for i in range(n, -1, -1):
		set_angle(i)
		dis = get_distance()
		format_(i, dis)
		time.sleep(0.1)
	stop_servo()
except KeyboardInterrupt:                       # Ctrl + C??????
	GPIO.cleanup()                              # GPIO????
	sys.exit()                                  # ???????



# ~ try:
	# ~ dis
	# ~ distance = '{:.1f}'.format(get_distance())  # ???1?????
	# ~ print("Distance: " + distance + "cm")       # ??
	# ~ time.sleep(1)                               # 1???

# ~ except KeyboardInterrupt:                       # Ctrl + C??????
	# ~ GPIO.cleanup()                              # GPIO????
	# ~ sys.exit()                                  # ???????





