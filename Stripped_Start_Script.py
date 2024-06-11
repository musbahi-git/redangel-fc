import RPi.GPIO as GPIO
import smbus
import time

# Setup for GPIO
motor_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

# Setup for MPU-6050
bus = smbus.SMBus(1)
mpu_address = 0x68

# Initialize MPU-6050
bus.write_byte_data(mpu_address, 0x6B, 0)  # Wake up the MPU-6050

def read_gyro():
    gyro_xout = bus.read_byte_data(mpu_address, 0x43) << 8 | bus.read_byte_data(mpu_address, 0x44)
    if gyro_xout > 32768:
        gyro_xout -= 65536
    return gyro_xout

try:
    while True:
        gyro_x = read_gyro()
        print("Gyro X:", gyro_x)

        # Simple control logic: if the gyro x-axis value exceeds a threshold, turn on the motor
        if abs(gyro_x) > 500:  # Adjust this threshold based on your needs
            GPIO.output(motor_pin, GPIO.HIGH)
        else:
            GPIO.output(motor_pin, GPIO.LOW)

        time.sleep(0.1)

finally:
    GPIO.cleanup()
