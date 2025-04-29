# keyboard-cyberdeck-pelicase-1150

Let's start with something simple: a 2x2 matrix keyboard using only 4 diodes, 4 pushbuttons, 4 resistors for pulldown and raspberry pi pico. 
The idea is to monitor which button is pressed using the pi GPIOs and program a small firmware to translate that to a keycode. 


```
        COL0   COL1
       +------+------+
ROW0 |  [A]  |  [B]  |
ROW1 |  [C]  |  [D]  |
       +------+------+
```



## WIP Raspberry Pi Pico HID Keyboard (CircuitPython)

### Requirements
- Raspberry Pi Pico
- CircuitPython firmware: [https://circuitpython.org/board/raspberry_pi_pico/](https://circuitpython.org/board/raspberry_pi_pico/)
- Adafruit HID library: [https://circuitpython.org/libraries](https://circuitpython.org/libraries)

### Setup
1. **Install CircuitPython**  
   - Hold BOOTSEL, plug in Pico → copy `.uf2` file to `RPI-RP2` drive.
   Alternatively use picotool (see below)
   Note: might need to mount manually
2. **Copy HID Library**  
   - From the Adafruit bundle, copy `lib/adafruit_hid/` to `CIRCUITPY/lib/`.
3. **Create `code.py`**  
   ```python
   import time
   import usb_hid
   from adafruit_hid.keyboard import Keyboard
   from adafruit_hid.keycode import Keycode

   time.sleep(2)
   kbd = Keyboard(usb_hid.devices)
   kbd.send(Keycode.A)
   ```

### Behavior
- Sends 'A' key 2 seconds after boot.
- Auto-runs on reset or USB plug-in.

### Optional (C Firmware)
Use `picotool` for `.uf2` flashing:
```bash
picotool load firmware.uf2 -f
```


