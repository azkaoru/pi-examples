# -*- coding: utf-8 -*-

# ライブラリ呼び出し部
import RPi.GPIO as GPIO	# GPIOライブラリを呼び出し
import time				# 時間関連のライブラリを呼び出し

# 初期設定部
GPIO.setmode( GPIO.BOARD )	# GPIOを端子番号で指定する
GPIO.setup(11, GPIO.IN )	# 18番端子を入力に設定する

# プログラム本体
while True:						# 繰り返しを行う
	if GPIO.input( 11 ) == 1:	# スイッチが押されているかを確認する
		print "ON"				# スイッチが押されている場合は「ON」と表示する
	else:
		print "OFF"				# スイッチが押されていない場合は「OFF」と表示する
	time.sleep(1)				# 1秒待機する
