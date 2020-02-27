# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse

import time
import redpitaya_scpi as scpi

rp_s = scpi.scpi('0')
# clear all leds
for i in range(8):
    rp_s.tx_txt('DIG:PIN LED' + str(i) + ',' + str(0))

# Start the system.
osc_startup()

# Make client channels to send packets.
osc_udp_client("10.0.10.101", 1234, "redpitaya")

# Build a simple message and send it.
msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
osc_send(msg, "redpitaya")

# Build a message with autodetection of data types, and send it.
msg = oscbuildparse.OSCMessage("/test/me", None, ["text", 672, 8.871])
osc_send(msg, "redpitaya")

# Buils a complete bundle, and postpone its executions by 10 sec.
# exectime = time.time() + 10   # execute in 10 seconds
msg1 = oscbuildparse.OSCMessage("/sound/levels", None, [1, 5, 3])
# msg2 = oscbuildparse.OSCMessage("/sound/bits", None, [32])
# msg3 = oscbuildparse.OSCMessage("/sound/freq", None, [42000])
# bun = oscbuildparse.OSCBundle(oscbuildparse.unixtime2timetag(exectime),
#                     [msg1, msg2, msg3])
# osc_send(bun, "redpitaya")

# Periodically call osc4py3 processing method in your event loop.
# finished = False
# while not finished:
#     # You can send OSC messages from your event loop too…
#     # …
#     rp_s.tx_txt('DIG:PIN LED1,1')
#     osc_process()
#     # …
#
# # Properly close the system.
# osc_terminate()


while(True):
    rp_s.tx_txt('DIG:PIN LED1,1')
    print("looping and sending osc, test")
    msg = oscbuildparse.OSCMessage("/test/me", ",sif", ["text", 672, 8.871])
    osc_send(msg, "redpitaya")
    osc_process()
    # time.sleep(1)
    rp_s.tx_txt('DIG:PIN LED1,0')
    time.sleep(0.5)


# # Properly close the system.
osc_terminate()
