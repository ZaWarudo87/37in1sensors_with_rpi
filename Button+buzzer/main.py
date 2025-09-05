import RPi.GPIO as GPIO 
import time

BTN_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(GPIO.input(BTN_PIN))
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()