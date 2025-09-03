import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LED_PIN, GPIO.OUT)

# digital
# GPIO.output(LED_PIN, GPIO.HIGH)

# analog
# p = GPIO.PWM(pin, frq)
# p.start(duty)
# p.ChangeDutyCycle(duty)
# p.stop()

GPIO.cleanup()