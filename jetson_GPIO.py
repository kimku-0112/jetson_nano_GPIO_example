import Jetson.GPIO as GPIO
import time

LED_PIN = 33

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, True)
print("LED turn on")
time.sleep(2.0)
GPIO.output(LED_PIN, False)
print("LED turn off")

GPIO.cleanup()
