# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# 브로드컴 방식 pin assign
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

try:
    while True:
        input_value = GPIO.input(18)

        if input_value == False:
            GPIO.output(23, True)
            time.sleep(0.1)

        else:
            GPIO.output(23, False)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()