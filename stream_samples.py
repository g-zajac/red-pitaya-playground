#!/usr/bin/python

import sys
import time
import redpitaya_scpi as scpi

from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse

rp_s = scpi.scpi('0')

# clear all leds
for i in range(8):
    rp_s.tx_txt('DIG:PIN LED' + str(i) + ',' + str(0))

# Start the system.
osc_startup()

# Make client channels to send packets.
osc_udp_client("10.0.10.101", 1234, "redpitaya")

# rp_s.tx_txt('ACQ:DEC 8')
rp_s.tx_txt('ACQ:DEC 8')
rp_s.tx_txt('ACQ:TRIG:LEV 0')
rp_s.tx_txt('ACQ:TRIG:DLY 0')

rp_s.tx_txt('ACQ:START')
rp_s.tx_txt('ACQ:TRIG NOW')
# rp_s.tx_txt('ACQ:TRIG EXT_PE')

while(True):
    rp_s.tx_txt('DIG:PIN LED1,1')

    while 1:
        rp_s.tx_txt('ACQ:TRIG:STAT?')
        if rp_s.rx_txt() == 'TD':
            break

    rp_s.tx_txt('ACQ:SOUR1:DATA:OLD:N? 50')
    buff_string = rp_s.rx_txt()
    # buff_string = buff_string.strip('{}\n\r').replace("  ", "").split(',')
    # buff = list(map(float, buff_string))

    print(buff_string)
    # msg = oscbuildparse.OSCMessage("/plant/voltage", ",sif", buff)
    # msg = oscbuildparse.OSCMessage("/plant/voltage", ",sif", ["text", 672, 8.871])
    # osc_send(msg, "redpitaya")
    # osc_process()

    rp_s.tx_txt('DIG:PIN LED1,0')
    time.sleep(1)


# osc_terminate()
