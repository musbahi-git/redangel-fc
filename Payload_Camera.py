from picamera import PiCamera
from time import sleep

camera = PiCamera()

try:
    # Start recording
    camera.start_recording('/home/pi/video.h264')

    # Keep the program running until it's interrupted
    while True:
        sleep(1)  # delay to reduce CPU usage

except KeyboardInterrupt:
    # Stop recording when the program is interrupted
    camera.stop_recording()

finally:
    # Ensure the camera is released properly
    camera.close()