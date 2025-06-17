from adafruit_circuitplayground import cp
import time
while True:
    if cp.switch:
        cp.red_led = True
        time.sleep(.5)
        cp.red_led = False
        time.sleep(.5)

    if cp.button_a:
        cp.play_file("applause_y.wav")

    if cp.button_b:
        cp.play_file("ahem_x.wav")

    if cp.touch_A1:
        cp.pixels[0] = (100, 100, 100)
        time.sleep(.5)
        cp.pixels[0] = (0, 0, 0)
        time.sleep(.5)

# Write your code here :-)
