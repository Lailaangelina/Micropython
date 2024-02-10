#Laila Murgo 1/20/24
#conditionals test

from include.rcc_library import Raft

myraft= Raft()

fav_color = "blue"
age = 16

if fav_color == "blue" and age > 13 :
    myraft.led_on()