from include.rcc_library import Raft

import utime

myraft = Raft()

for i in range(28):
    myraft.led_on()
    utime.sleep_ms(400)
    myraft.led_off()
    utime.sleep_ms(90)