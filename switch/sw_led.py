# -*- coding: utf-8 -*-


# ライブラリ呼び出し部
import RPi.GPIO as GPIO	# GPIOライブラリを呼び出し

# 初期設定部
GPIO.setmode( GPIO.BOARD )	# GPIOを端子番号で指定する
GPIO.setup( 16, GPIO.OUT )	# 16番端子を出力に設定する
GPIO.setup( 18, GPIO.IN )	# 18番端子を入力に設定する

# プログラム本体
while True:								# 繰り返しを行う
	if GPIO.input( 18 ) == GPIO.HIGH:	# スイッチが押されているかを確認する
		GPIO.output( 16, GPIO.HIGH )	# 押されている場合はLEDを点灯
	else:
		GPIO.output( 16, GPIO.LOW )		# 押されている場合はLEDを消灯

