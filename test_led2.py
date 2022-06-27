from brightpi import *
import time

brightSpecial = BrightPiSpecialEffects()
brightSpecial.reset()

led_white = [1,2,3,4]
led_ir = [5,6,7,8]## in pairs ##8 ir
led_all = [1,2,3,4,5,6,7,8]

def led_on(leds):
    brightSpecial.set_led_on_off((1,2,3,4), 1)
def led_off(leds):
    brightSpecial.set_led_on_off((1,2,3,4), 0)

def brightness_adjust(brightness):
    brightSpecial.set_gain(brightness)# 0<=gain<=15


if __name__ == '__main__':
    while(True):
        led_on(leds=led_all)
        time.sleep(3)
        led_off(leds=led_all)
        time.sleep(3)