from time import sleep
import RPi.GPIO as GPIO

# Setting up GPIO pins for direction and step
DIR = 20   # Pin arah gerakan
STEP = 21  # Pin langkah

# Defining clockwise and counterclockwise rotation
CW = 1     # Putaran searah jarum jam
CCW = 0    # Putaran berlawanan arah jarum jam

# Steps per Revolution (360 / 7.5)
SPR = 48   # Langkah per Putaran

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

# Setting up microstep resolution GPIO pins
MODE = (14, 15, 18)   # Pin GPIO Resolusi Mikro
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

# Setting microstepping resolution to 1/32
GPIO.output(MODE, RESOLUTION['1/32'])

# Function to rotate stepper motor based on input degrees
def rotate_stepper(degrees):
    # Calculate total steps for given degrees
    total_steps = int((degrees / 360) * SPR * 32)
    # Rotate motor based on direction
    if degrees >= 0:
        GPIO.output(DIR, CW)  # Clockwise rotation
    else:
        GPIO.output(DIR, CCW) # Counterclockwise rotation
    # Perform the rotation
    for _ in range(total_steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

# Example usage: Rotate stepper motor 90 degrees clockwise // This Is Adjustable bisa pakai input for testing
rotate_stepper(90)

# Cleaning up GPIO
GPIO.cleanup()
