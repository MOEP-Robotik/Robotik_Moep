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

TOPLEFT.run_angle(1000, 300, wait=False)
BEWEGUNGSMOTOREN.straight(700)
BEWEGUNGSMOTOREN.settings(straight_speed=900)
BEWEGUNGSMOTOREN.straight(-200)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
TOPLEFT.run_angle(1000, -320)
BEWEGUNGSMOTOREN.straight(200)

BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(170)
TOPRIGHT.run_angle(1000, -90)

BEWEGUNGSMOTOREN.straight(-170)
BEWEGUNGSMOTOREN.turn(45)
BEWEGUNGSMOTOREN.straight(-800)

TOPRIGHT.run_angle(1000, 90)