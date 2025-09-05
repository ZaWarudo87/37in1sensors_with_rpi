import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
# GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # digital
        # GPIO.output(LED_PIN, GPIO.HIGH)

        # analog
        # p = GPIO.PWM(pin, frq)
        # p.start(duty)
        # p.ChangeDutyCycle(duty)
        # p.stop()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()