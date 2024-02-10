from machine import Pin, PWM
import utime

color1 = PWM(Pin(18))
color1.freq(500)

color2 = PWM(Pin(16))
color2.freq(500)

for i in range(100):
    color1.duty_u16(i*655)
    color2.duty_u16((200-i)*655)
    utime.sleep_ms(100)