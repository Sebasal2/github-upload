"""
Project doc:
https://docs.google.com/document
/d/18vhj9y9asoieNgy-0aGClKWLwEajTrr24bHdN3u6QP0/edit#
"""
# import modules
import time
from gpiozero import LED, Button, LEDBoard
from signal import pause
from time import sleep

#imports position on board
leds = LEDBoard(17,27,22,18)

#import button
button = Button(3)
count = 0

#starts loop for LEDs
while 1:
  #button is pressed and lights turns on
  if button.is_pressed and count == 0:
    count = 1
    print(count)
    leds.on()
    sleep(0.5)
  #button is pressed and lights begin blinking
  elif button.is_pressed and count == 1:
    count = 2
    print(count)
    leds.blink()
    sleep(0.5)
  #button is pressed and lights turn off
  elif button.is_pressed and count == 2:
    count = 0
    print(count)
    leds.off()
    sleep(0.5)
pause()


"""
Ground: 3 top to bottom on the right side
Button: 3 top to bottom on left side
Red light: 6 top to bottom left
Yellow light: 7 top to bottom left
Green light: 8 top to bottom left
Blue light: 6 top to bottom right
"""
