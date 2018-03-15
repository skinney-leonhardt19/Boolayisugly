import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.pinMode(17, RPL.INPUT)

while True:
    readSensor == RPLdigitalRead(17)
    if readSensor == 0:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(1, 0)
    if readSensor == 1:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(1, 1000)
    
