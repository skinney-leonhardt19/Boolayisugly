import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

import time

RPL.pinMode(17, RPL.INPUT)

while True:
    sensorRead == RPL.digitalRead(17) 
    if sensorRead == 1:
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
    if sensorRead == 0:
        RPL.servoWrite(0, 1500)
        RPL.servoWrite(1, 2000)
