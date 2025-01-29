# CircuitPython code that runs on a raspberry pi pico (rp2040 microcontroller)

import time
import board
import usb_cdc
import usb_hid
import digitalio

# Interface Setup
led_pin = board.GP15
btn_pin = board.GP20

# Incoming Setup
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

# Outgoing Setup
button = digitalio.DigitalInOut(btn_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    # Incoming Loop
    if usb_cdc.console.in_waiting > 0:
        signal = usb_cdc.console.read(usb_cdc.console.in_waiting).decode('utf-8').strip()
        if signal == "PICO_LED_ON":
            led.value = True
        elif signal == "PICO_LED_OFF":
            led.value = False

    # Outgoing Loop
    if not button.value:
        usb_cdc.console.write(b"SBC_LED_ON")
    else:
        usb_cdc.console.write(b"SBC_LED_OFF")
    time.sleep(0.1)
