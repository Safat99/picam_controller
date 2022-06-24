from brightpi import *

brightpi = BrightPi()
brightpi.reset()

led_white = [1,2,3,4]
led_ir = [5,6,7,8]## in pairs ##8 ir
led_all = [1,2,3,4,5,6,7,8]

def led_on(brightness,leds):
    brightpi.set_gain(brightness)
    brightpi.set_led_on_off(leds, ON)

def led_off(leds):
    brightpi.set_led_on_off(leds,OFF)

def ir_on():
    brightpi.set_gain(15)
    brightpi.set_led_on_off(led_ir, ON)

def ir_off():
    brightpi.set_led_on_off(led_ir, OFF)

