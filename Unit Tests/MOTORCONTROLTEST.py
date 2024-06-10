from adafruit_motorkit import MotorKit
kit = MotorKit()

kit.motor1.throttle = 1.0  # Full speed forward
kit.motor1.throttle = -1.0 # Full speed backward
kit.motor1.throttle = 0.0  # Stop
 