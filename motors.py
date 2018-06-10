# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time #

# Set GPIO Modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 9
pinMotorABackwards = 10
pinMotorBForwards = 7
pinMotorBBackwards = 8

pinOnOff = 23


# Set the GPIO Pin mode
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)

GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)

GPIO.setup(pinOnOff, GPIO.IN)

def forwardsA():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)

def forwardsB():
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)   

def backwardsA():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)

def backwardsB():
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)   


def stopA():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)

def stopB():
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)    

def stopMotors():
    stopA()
    stopB()

def forwards():
    forwardsA()
    forwardsB()

def backwards():
    backwardsA()
    backwardsB()

def left():
    backwardsA()
    forwardsB()

def right():
    backwardsB()
    forwardsA()    

def isOn():
    GPIO.input(pinOnOff)


while True:            # this will carry on until you hit CTRL+C  
    if GPIO.input(23): # if port 25 == 1  
        print ("Port 24 is 1/HIGH/True - LED ON"         )
    else:  
        print ("Port 25 is 0/LOW/False - LED OFF"  )
    time.sleep(1)         # wait 0.1 seconds  
# Moving the robot

##forwards()
##time.sleep(1) # Pause for 1 second
##left()
##time.sleep(0.5) # Pause for half a second
##forwards()
##time.sleep(1)
##right()
##time.sleep(0.5)
##backwards()
##time.sleep(0.5)
##stopmotors()
