from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time

# Create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# Create a DC motor object.
# The motor is connected to port M1 (change this to the port where your motor is connected).
motor = mh.getMotor(1)

try:
    # Set the speed and run the motor forward
    motor.setSpeed(255)
    motor.run(Adafruit_MotorHAT.FORWARD)
    time.sleep(2)

    # Run the motor backward
    motor.run(Adafruit_MotorHAT.BACKWARD)
    time.sleep(2)

    # Stop the motor
    motor.run(Adafruit_MotorHAT.RELEASE)
    time.sleep(2)

except KeyboardInterrupt:
    # Release the motor on a KeyboardInterrupt.
    motor.run(Adafruit_MotorHAT.RELEASE)