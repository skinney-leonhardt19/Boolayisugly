import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

def servomove(x):
    if x == 0:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
    if x == 1:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 1000)
        
RPL.pinMode(17, RPL.INPUT)

if RPL.digitalRead(17) == 1:
    servomove(1)
if RPL.digitalRead(17) == 0:
    servomove(0)
