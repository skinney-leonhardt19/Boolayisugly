import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

RPL.pinMode(17, RPL.INPUT)

while RPL.digitalRead(17) == 0:
    RPL.servoWrite(0, 0)
    RPL.servoWrite(1, 0)
    break
while RPL.digitalRead(17) == 1:
    RPL.servoWrite(0, 2000)
    RPL.servoWrite(1, 1000)
    break
