#Laila Murgo 1/20/24
#Makes the led blink

from include.rcc_library import Raft
import utime

myraft = Raft()

myraft.led_on()
utime.sleep_ms(1000)
myraft.led_off()

myraft.led_on()
utime.sleep_ms(2000)
myraft.led_off()

myraft.led_on()
utime.sleep_ms(1000)
myraft.led_off()