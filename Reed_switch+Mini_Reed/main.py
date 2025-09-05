import RPi.GPIO as GPIO 
import time

AO_PIN = 2
DO_PIN = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(AO_PIN, GPIO.IN)
GPIO.setup(DO_PIN, GPIO.IN)

try:
    while True:
        print(f"AO: {GPIO.input(AO_PIN)}, DO: {GPIO.input(DO_PIN)}")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()