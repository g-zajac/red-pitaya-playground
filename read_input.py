# read_input.py
from redpitaya.overlay.mercury import mercury as FPGA
overlay = FPGA()
GPIO = FPGA.gpio
gpio_i = GPIO('n', 2, "in")
import time
while True:
    x=gpio_i.read()
    print(x)
    time.sleep(0.5)
