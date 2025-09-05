import RPi.GPIO as GPIO 
import time

BTN_PIN = 2
BUZZER_PIN = 3
beep = False
bef_btn = False
now_btn = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    while True:
        now_btn = GPIO.input(BTN_PIN)
        if now_btn != bef_btn and not now_btn:
            beep = not beep
            GPIO.output(BUZZER_PIN, beep)
            print("beeping" if beep else "stopped")
        bef_btn = now_btn
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()