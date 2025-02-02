
import platform 
if platform.system() == 'Darwin':
    #my_dev_flag = True
    print('Operating in DEVMODE!')
    import sys
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
    sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

import I2CDevice
import time

t1 = 0.2
t2 = 1
t3 = 3

ledarr = I2CDevice.I2CDevice(0x08)
ledarr.send("CLEAR")
time.sleep(2)

ledarr.send("SETPRE", 0)  # setze Pattern 0 aktiv (ohne zu laden)
time.sleep(t1)
ledarr.send("FLYBY", 0)  # setze "normalen" editiermodus Modus

time.sleep(t1)
ledarr.send("DRVX", 1000)
time.sleep(t1)
ledarr.send("DRVX", -1000)
time.sleep(t1)

ledarr.send("DRVY", 1000)
time.sleep(t1)
ledarr.send("DRVY", -1000)
time.sleep(t1)

ledarr.send("DRVZ", 1000)
time.sleep(t1)
ledarr.send("DRVZ", -1000)
time.sleep(t1)