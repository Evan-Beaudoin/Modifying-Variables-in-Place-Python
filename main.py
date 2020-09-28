#Created By: Evan
#Created on: Sept. 2020

#This program: Changes Variable

from microbit import *

hungryness = 0

while True:

    if button_a.is_pressed():
        hungryness = hungryness + 1
        sleep(100)
    if button_b.is_pressed():
        hungryness = hungryness - 1
        sleep(100)
    
    display.show(hungryness)
    sleep(50)
