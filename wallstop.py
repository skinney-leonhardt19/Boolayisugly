import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

import time

RPL.pinMode(17, RPL.input)

motorR = 1
motorL = 0

s = 4.8

    sensorRead == RPL.digitalRead(17)
    while sensorRead == 1:
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
    while sensorRead == 0:
        sec = time.time()
        while time.time() < (sec + s)
            RPL.servoWrite(0, 1490)
            RPL.servoWrite(1, 1510)
        while time.time() > (sec + s)
            RPL.servoWrite(0, 0)
            RPL.servoWrite(1, 0)

    
