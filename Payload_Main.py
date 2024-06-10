# Import the necessary libraries
from adafruit_motorkit import MotorKit
import smbus
import math

# Initialize the MotorKit object
kit = MotorKit()

# Initialize the I2C bus
bus = smbus.SMBus(1)

# This is the address of the GY-521 sensor
address = 0x68

# Wake up the GY-521 sensor
bus.write_byte_data(address, 0x6b, 0)

# Function to read raw data from accelerometer
def read_raw_data(addr):
    high = bus.read_byte_data(address, addr)
    low = bus.read_byte_data(address, addr+1)
    
    # Concatenate higher and lower value
    value = ((high << 8) | low)
        
    # Get signed value from raw 16-bit value
    if(value > 32768):
        value = value - 65536
    return value

# Main loop
while True:
    # Read accelerometer data
    acc_x = read_raw_data(0x3b)
    acc_y = read_raw_data(0x3d)
    acc_z = read_raw_data(0x3f)

    # Get the absolute value of the x, y and z accelerometer readings
    abs_acc_x = abs(acc_x)
    abs_acc_y = abs(acc_y)
    abs_acc_z = abs(acc_z)

    # Calculate the total acceleration
    total_acc = abs_acc_x + abs_acc_y + abs_acc_z

    # Normalize the total acceleration to a value between 0 and 1
    # This will be used to set the motor speed
    # Note: The value 16384 comes from the sensitivity of the GY-521 sensor for a range of +/-2g
    # You may need to adjust this value depending on the sensitivity setting of your sensor
    normalized_acc = total_acc / (3 * 16384)

    # Determine the direction based on the sign of the x-axis accelerometer reading
    direction = 1.0 if acc_x >= 0 else -1.0

    # Set the motor speed and direction based on the normalized acceleration and direction
    kit.motor1.throttle = direction * normalized_acc