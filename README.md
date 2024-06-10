## Simplified Wiring Instructions:
1. Power Supplies:

    Connect the power supply to the Raspberry Pi Zero.
    Connect the separate power supply to the STARLIGHT flight computer.

2. Connecting the Raspberry Pi Zero to the Adafruit Motor Shield v2:

    The Adafruit Motor Shield v2 communicates via I2C.
    Connect the SDA (data line) on the Raspberry Pi GPIO2 (pin 3) to SDA on the Motor Shield.
    Connect the SCL (clock line) on the Raspberry Pi GPIO3 (pin 5) to SCL on the Motor Shield.
    Connect the GND on the Raspberry Pi GPIO6 (pin 9) to GND on the Motor Shield.
    Connect the 3.3V or 5V power pin on the Raspberry Pi to the VIN pin on the Motor Shield (if the Motor Shield requires it; usually it is powered separately).

3. Connecting the DC Motor to the Motor Shield:

    Connect the DC motor wires to the terminal block M1 (or M2, M3, M4 depending on your motor shield's configuration) on the Motor Shield.

4. Connecting the GPS Module to the Raspberry Pi Zero:

    The GPS module usually communicates via UART.
    Connect the GPS TX (transmit) pin to the Raspberry Pi RX (receive) pin GPIO15 (pin 10).
    Connect the GPS RX (receive) pin to the Raspberry Pi TX (transmit) pin GPIO14 (pin 8).
    Connect the GND pin on the GPS to a GND pin on the Raspberry Pi.
    Connect the VCC pin on the GPS to a 3.3V or 5V pin on the Raspberry Pi (depending on your GPS module's voltage requirements).

5. Connecting the Camera Module to the Raspberry Pi Zero:

    Connect the camera module to the camera interface (CSI) on the Raspberry Pi Zero using the camera ribbon cable.

6. Connecting the STARLIGHT Flight Computer to the Raspberry Pi Zero:

    The STARLIGHT flight computer will send accelerometer data to the Raspberry Pi.
    Identify the communication protocol (e.g., UART, I2C, SPI) used by the flight computer to send data.
        For UART:
            Connect the TX pin of the flight computer to the RX pin GPIO15 (pin 10) on the Raspberry Pi.
            Connect the RX pin of the flight computer to the TX pin GPIO14 (pin 8) on the Raspberry Pi.
        For I2C:
            Connect the SDA pin of the flight computer to SDA on the Raspberry Pi GPIO2 (pin 3).
            Connect the SCL pin of the flight computer to SCL on the Raspberry Pi GPIO3 (pin 5).

## Electronics Initialisation 

### Complete manufacturer set up for flight computer
[STARLIGHT_README.md]


### Raspberry Pi Commands 

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python3-pip

pip3 install Adafruit-MotorHAT

sudo raspi-config
   
    >>> To enable I2C on your Raspberry Pi, you can use the raspi-config utility. Here are the steps:

        Open a terminal on your Raspberry Pi.

        Enter the following command to open the configuration utility:
        'sudo raspi-config'
            > Use the arrow keys to navigate to 5 Interfacing Options and press Enter.
            Navigate to P5 I2C and press Enter.

            When asked Would you like the ARM I2C interface to be enabled?, select <Yes> and press Enter.

            You will see a message saying The ARM I2C interface is enabled. Press Enter to continue.

            Finally, select <Finish> to exit the configuration utility. 

        'sudo reboot'
        #### Confirms I2C is enabled. Could be useful.
        'ls /dev/*i2c*'


sudo apt-get install python3-smbus

---

## Pre-Launch Sequence

### Starlight-RedAngel Calibration Script

- Place the STARLIGHT board on a flat and level surface.
- Run RedStartup1.py
    Code walkthrough:
    - Take multiple readings from the accelerometer while the board is at rest.
    - Calculate the average of these readings. This will be the bias.
    - Subtract the bias from future accelerometer readings to correct them.

### Run Calibration before continuing start up sequence.

