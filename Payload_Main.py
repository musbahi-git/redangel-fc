import time
import smbus
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# Create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# Create a DC motor object.
# The motor is connected to port M1 (change this to the port where your motor is connected).
motor = mh.getMotor(1)

# Set the speed of the motor (0 is off, 255 is max speed).
motor.setSpeed(150)

# GY-521 module constants
GY521_ADDRESS = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B

# Initialize the bus and the sensor.
bus = smbus.SMBus(1)
bus.write_byte_data(GY521_ADDRESS, PWR_MGMT_1, 0)

def read_word(sensor_address, register):
    high = bus.read_byte_data(sensor_address, register)
    low = bus.read_byte_data(sensor_address, register + 1)
    value = (high << 8) + low
    return value - 65536 if value >= 0x8000 else value

try:
    while True:
        # Read the accelerometer data.
        accel_x = read_word(GY521_ADDRESS, ACCEL_XOUT_H)

        # Use the accelerometer data to control the motor.
        if accel_x > 0:
            motor.run(Adafruit_MotorHAT.FORWARD)
        else:
            motor.run(Adafruit_MotorHAT.BACKWARD)

        # Adjust the speed based on the magnitude of the acceleration.
        speed = min(int((abs(accel_x) / 16384.0) * 255), 255)
        motor.setSpeed(speed)

        time.sleep(0.1)

except KeyboardInterrupt:
    # Release the motor on a KeyboardInterrupt.
    motor.run(Adafruit_MotorHAT.RELEASE)