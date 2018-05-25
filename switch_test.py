#!/usr/bin/python3
#coding: utf-8

#インポート
import RPi.GPIO as GPIO  #RaspberryPiのFPIO用
import time
from psonic import *  #sonic-pi用

#GPPIOの初期設定
GPIO.setmode(GPIO.BOARD) #PhysicalでのPin番号指定
GPIO.setup(11, GPIO.IN)  #Pin11をinput設定


#動作本体
for i in range(50):
    PLAY_TRIGGER = GPIO.input(11)
    print(PLAY_TRIGGER)
    if PLAY_TRIGGER != 0:
        play(75)
    sleep(0.25)

#終了動作
GPIO.cleanup()  #GPIOピンの設定をリセット


