# RaspberryPi.py
import smbus
import time
import math
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# DC motor on M2
motor = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
motor.setSpeed(150)
motor.run(Adafruit_MotorHAT.FORWARD)

# Initialize I2C bus
bus = smbus.SMBus(1)
address = 0x05

while True:
    # Read accelerometer data from I2C
    # The data is a list of three values: [x, y, z]
    data = bus.read_i2c_block_data(address, 0, 3)
    x, y, z = data

    # Calculate the magnitude of the acceleration vector
    # This gives a measure of the overall acceleration, regardless of the direction
    magnitude = math.sqrt(x**2 + y**2 + z**2)

    # Map the magnitude to the motor speed (assuming the magnitude is in the range 0-255)
    # This will control the speed of the motor based on the overall acceleration
    speed = min(max(int(magnitude), 0), 255)

    # Set the motor speed
    motor.setSpeed(speed)

    # Control the motor direction based on the x value
    # If x is positive, the motor will run forward, otherwise it will run backward
    # This will cause the motor to rotate in the opposite direction when the flight computer turns
    if x > 0:
        motor.run(Adafruit_MotorHAT.FORWARD)
    else:
        motor.run(Adafruit_MotorHAT.BACKWARD)

    # Wait for a short period of time before the next iteration
    # This allows the motor to respond to the commands
    time.sleep(0.1)