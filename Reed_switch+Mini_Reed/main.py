import RPi.GPIO as GPIO
import serial
import time

D0_PIN = 2
ser = serial.Serial("/dev/serial0", 115200, timeout=1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(D0_PIN, GPIO.IN)

try:
    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            A0 = int(line)
        else:
            A0 = 0
        print(f"A0: {A0}, D0: {GPIO.input(D0_PIN)}")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()