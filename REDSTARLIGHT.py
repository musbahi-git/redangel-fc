# STARLIGHT_board.py
import starlight
import machine
import time

# initialize I2C in order to talk to the ICM-42605 and BMP388 on-board. Pins 3 and 2 are the SCL and SDA pins respectively on STARLIGHT
i2c = machine.I2C(1, scl=machine.Pin(3), sda=machine.Pin(2), freq=9600)

gyr = starlight.ICM42605(i2c, 0x68) # create our ICM-42605 object
gyr.config_gyro() # set up our gyroscope/accelerometer
gyr.enable() # enable our gyroscope/accelerometer
gyr.get_bias() # calibrate our gyroscope/accelerometer

count = 0
start = time.ticks_ms()
while True: # our main loop
    gyr.updateData(time.ticks_diff(time.ticks_ms(), start)) # Update gyroscope data, this should be ran as fast as your loop refresh rate
    start = time.ticks_ms()
    count += 1
    time.sleep_ms(20)
    if count % 50 == 0:
        # X Y and Z are the board's rotation
        # send accelerometer data to Raspberry Pi over I2C
        i2c.writeto(0x05, bytearray([gyr.gx, gyr.gy, gyr.gz]))