int analogPin = 35;
int sensorValue = 0;

void setup() {
    pinMode(analogPin, INPUT);
    Serial.begin(115200); // TX=GPIO1, RX=GPIO3
}

void loop() {
    Serial.println(analogRead(analogPin));
    delay(500);
}
