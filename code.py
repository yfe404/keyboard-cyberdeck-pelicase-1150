import board
import digitalio
import time
from digitalio import DigitalInOut, Direction, Pull

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

rowPins = [
    digitalio.DigitalInOut(board.GP2), 
    digitalio.DigitalInOut(board.GP3)
];
colPins = [
    digitalio.DigitalInOut(board.GP4), 
    digitalio.DigitalInOut(board.GP5)
];  

keymap = [
  [Keycode.A, Keycode.B],
  [Keycode.C, Keycode.D]
]

# Setup row pins as outputs
for rowPin in rowPins:
    rowPin.direction = Direction.OUTPUT
    rowPin.value = 1

# Setup column pins as inputs with pullups
for colPin in colPins:
    colPin.direction = Direction.INPUT
    colPin.pull = Pull.UP


while True:
    for row, rowPin in enumerate(rowPins):
        rowPin.value = 0
        for col, colPin in enumerate(colPins):
            if not colPin.value:
                kbd.send(keymap[row][col])
                time.sleep(0.2)
        rowPin.value = 1

