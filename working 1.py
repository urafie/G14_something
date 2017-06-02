from microbit import *

while True:
    if pin0.read_digital() == 1:
        while pin0.read_digital() == 1:
            pin1.write_analog(1023)
            sleep(700)
            pin1.write_analog(0)
            sleep(700)