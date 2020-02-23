from redpitaya.overlay.mercury import mercury as FPGA
overlay = FPGA()
LED = FPGA.led
led1 = LED(3, 0)
# blink 10 times
import time
for _ in range(10):
    led1.write(1)
    time.sleep(0.1)
    led1.write(0)
    time.sleep(0.1)
led1.close()
