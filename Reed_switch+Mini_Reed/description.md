# Reed switch磁簧開關 & Mini Reed迷你磁簧 & Flame火焰
## Description
可以感應是否有磁鐵靠近的奇妙裝置。

### 大磁簧模組
這個模組相較於迷你磁簧，有A0和D0腳位。其中A0腳位輸出最高5V的類比訊號，因此我們需要將這個腳位用分壓電路接到ESP32上，以便觀測。

### 小磁簧模組
不像大磁簧模組具備類比輸出腳位，並且訊號腳位是上拉電阻的感覺，沒有磁訊號是1，有是0。

**照片待補**

## Code
```python
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
```