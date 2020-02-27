#!/usr/bin/python

import sys
import time
import redpitaya_scpi as scpi

rp_s = scpi.scpi('0')

# clear all leds
for i in range(8):
    rp_s.tx_txt('DIG:PIN LED' + str(i) + ',' + str(0))

# time.sleep(3)
# script started
print('script started')
rp_s.tx_txt('DIG:PIN LED0,1')

rp_s.tx_txt('ACQ:START')
rp_s.tx_txt('ACQ:TRIG NOW')
rp_s.tx_txt('DIG:PIN LED1,1')

while 1:
    rp_s.tx_txt('ACQ:TRIG:STAT?')
    if rp_s.rx_txt() == 'TD':
        break

rp_s.tx_txt('ACQ:SOUR1:DATA?')
buff_string = rp_s.rx_txt()
buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
buff = list(map(float, buff_string))

print(buff)
rp_s.tx_txt('DIG:PIN LED1,0')
