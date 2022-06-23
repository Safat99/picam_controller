from brightpi import *
import time

brightpi = BrightPi()
brightpi.reset()

led_white = [1,2,3,4]
led_ir = [5,6,7,8]## in pairs ##8 ir
led_all = [1,2,3,4,5,6,7,8]

def led_on(leds):
    brightpi.set_led_on_off(leds, ON)
def led_off(leds):
    brightpi.set_led_on_off(leds,OFF)

def brightness_adjust(brightness):
    brightpi.set_gain(brightness)# 0<=gain<=15


if __name__ == '__main__':
    while(True):
        led_on(leds=led_all)
        time.sleep(3)
        led_off(leds=led_all)
        time.sleep(3)