import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

import sys, tty, termios, signal

import time

RPL.pinMode(17, RPL.input)

motorR == 1
motorL == 0

while True:
    sensorRead == RPL.digitalRead(17)
 global move == time.time 
    if sensorRead == 1:
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
    if sensorRead == 0:
        RPL.servoWrite(0, 1490)
        RPL.servoWrite(1, 1510)
    if move == time.time + 3:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)

    
