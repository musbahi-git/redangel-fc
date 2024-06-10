#!/bin/bash

# Import the necessary libraries
import RPi.GPIO as GPIO
from gpiozero import LED
from picamera import PiCamera
from time import sleep
from adafruit_motorkit import MotorKit
import smbus
import math

# Initialize the LED on GPIO 17
led = LED(17)

# Initialize the 7-segment display
# You'll need to replace these pin numbers with the actual pin numbers you're using
segments = (11, 4, 23, 8, 7, 10, 18, 25)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# Function to display a number on the 7-segment display
def display_number(num):
    # You'll need to replace these values with the actual values for your 7-segment display
    numbers = {
        '1': (0, 1, 1, 0, 0, 0, 0),
        '2': (1, 1, 0, 1, 1, 0, 1),
        '3': (1, 1, 1, 1, 0, 0, 1),
        '4': (0, 1, 1, 0, 0, 1, 1)
    }
    for i in range(7):
        GPIO.output(segments[i], numbers[str(num)][i])

# Function to flash the LED
def flash_led():
    led.on()
    sleep(1)
    led.off()

# Function to test the accelerometer data
def test_accelerometer():
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

    # Read accelerometer data
    acc_x = read_raw_data(0x3b)
    acc_y = read_raw_data(0x3d)
    acc_z = read_raw_data(0x3f)

    # Print the accelerometer data
    print("Accelerometer data: X = {}, Y = {}, Z = {}".format(acc_x, acc_y, acc_z))

# Function to record video
def record_video():
    # Initialize the PiCamera object
    camera = PiCamera()

    # Start recording
    camera.start_recording('/home/pi/video.h264')

    # Wait for the Raspberry Pi to shut down
    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            break

    # Stop recording
    camera.stop_recording()

# Flash the LED and display '1' on the 7-segment display
flash_led()
display_number(1)

# Run MOTORCONTROLTEST.py
python3 MOTORCONTROLTEST.py

# If the script finishes successfully, flash the LED and display '2' on the 7-segment display
if [ $? -eq 0 ]; then
    flash_led()
    display_number(2)
fi

# Start recording video
record_video()

# Flash the LED and display '3' on the 7-segment display
flash_led()
display_number(3)

# Test the accelerometer data
test_accelerometer()

# Flash the LED and display '4' on the 7-segment display
flash_led()
display_number(4)

# Start the main Payload_Main.py function
python3 Payload_Main.py