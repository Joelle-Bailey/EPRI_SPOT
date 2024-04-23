##############################################################################
#                               Motor Current
# Motor Current module
#
# Created by Joelle Bailey for EPRI_SPOT, Spring 2024
##############################################################################

import RPi.GPIO as GPIO

class MotorCurrent:
    def __init__(self, isr, pin_number = 18):
        self.pin_number = pin_number

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN)

        GPIO.add_event_detect(self.pin_number, GPIO.RISING,
            callback=isr, bouncetime=300)