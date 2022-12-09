import screen_brightness_control as sbc

# get the brightness
brightness = sbc.get_brightness()
# get the brightness for the primary monitor
primary = sbc.get_brightness(display=0)

# set the brightness to 100%
sbc.set_brightness(100)
# set the brightness to 100% for the primary monitor
sbc.get_brightness(100, display=0)

# show the current brightness for each detected monitor
for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')


# https://www.geeksforgeeks.org/how-to-control-laptop-screen-brightness-using-python/
# https://morioh.com/p/2e255e407f4a