import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def servomove(x):
if x == 1:
    RPL.servoWrite(0, 2000)
    RPL.servoWrite(1, 1000)
if x == 0:
    RPL.servoWrite(0, 0)
    RPL.servoWrite(1, 0)

RPL.pinMode(16, RPL.INPUT)

while True:
    sensorRead == RPL.digitalRead(16)
    if sensorRead == 1:
        servomove(1)
    else:
        servomove(0)
        RPL.servoWrite(0, 1000)
        RPL.servoWrite(1, 2000)
