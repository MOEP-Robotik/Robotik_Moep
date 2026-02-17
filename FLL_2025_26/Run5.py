from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)

TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)

BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.straight(560)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(200)
BEWEGUNGSMOTOREN.turn(135)
BEWEGUNGSMOTOREN.straight(-875)
BEWEGUNGSMOTOREN.turn(-90)
TOPLEFT.run_angle(600, -1500)
BEWEGUNGSMOTOREN.straight(50)
TOPLEFT.run_angle(600, 250, wait=False)