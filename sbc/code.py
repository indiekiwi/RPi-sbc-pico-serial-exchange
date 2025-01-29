# runs on raspberry pi sbc (single board computer)

import time
import serial
import RPi.GPIO as GPIO
from gpiozero import Button

# Interface Setup
led_pin = 16
btn = Button(20)
ser = serial.Serial('/dev/ttyACM0', 9600)

# Incoming Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

print("Starting...")

try:
    while True:
        # Incoming Loop
        if ser.in_waiting > 0:
            signal = ser.read(ser.in_waiting).decode('utf-8').strip()
            if signal == "SBC_LED_ON":
                print("Button pressed on PICO")
                GPIO.output(led_pin, GPIO.HIGH)
            elif signal == "SBC_LED_OFF":
                GPIO.output(led_pin, GPIO.LOW)

        # Outgoing Loop
        if btn.is_pressed:
            print("Button pressed on SBC")
            ser.write(b'PICO_LED_ON')
        else:
            ser.write(b'PICO_LED_OFF')

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program terminated.")
    ser.close()
    GPIO.cleanup()
