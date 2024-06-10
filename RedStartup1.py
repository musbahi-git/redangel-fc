import starlight
import machine
import time

# initialize I2C in order to talk to the ICM-42605 and BMP388 on-board. Pins 3 and 2 are the SCL and SDA pins respectively on STARLIGHT
i2c = machine.I2C(1, scl=machine.Pin(3), sda=machine.Pin(2), freq=9600)

gyr = starlight.ICM42605(i2c, 0x68) # create our ICM-42605 object
gyr.config_gyro() # set up our gyroscope/accelerometer
gyr.enable() # enable our gyroscope/accelerometer

# Take multiple readings and calculate the average
num_readings = 100
total_x, total_y, total_z = 0, 0, 0
for _ in range(num_readings):
    gyr.updateData(time.ticks_diff(time.ticks_ms(), start)) # Update gyroscope data, this should be ran as fast as your loop refresh rate
    start = time.ticks_ms()
    total_x += gyr.gx
    total_y += gyr.gy
    total_z += gyr.gz
    time.sleep_ms(20)

bias_x = total_x / num_readings
bias_y = total_y / num_readings
bias_z = total_z / num_readings

# Now you can subtract the bias from future readings to correct them
while True:
    gyr.updateData(time.ticks_diff(time.ticks_ms(), start)) # Update gyroscope data, this should be ran as fast as your loop refresh rate
    start = time.ticks_ms()
    corrected_x = gyr.gx - bias_x
    corrected_y = gyr.gy - bias_y
    corrected_z = gyr.gz - bias_z
    time.sleep_ms(20)