from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 50, 107)
BEWEGUNGSMOTOREN.use_gyro(True)
BEWEGUNGSMOTOREN.settings(straight_speed=800)

#TOPLEFT = Motor(Port.A)
#TOPRIGHT = Motor(Port.E)
BEWEGUNGSMOTOREN.straight(100)
BEWEGUNGSMOTOREN.straight(-50)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(80)
BEWEGUNGSMOTOREN.turn(210)
BEWEGUNGSMOTOREN.straight(-40)
BEWEGUNGSMOTOREN.straight(-100)
BEWEGUNGSMOTOREN.straight(100)
BEWEGUNGSMOTOREN.turn(105)
BEWEGUNGSMOTOREN.straight(-50)
