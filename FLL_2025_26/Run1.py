from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)
TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)

BEWEGUNGSMOTOREN.settings(straight_speed=800)

BEWEGUNGSMOTOREN.straight(570)
BEWEGUNGSMOTOREN.settings(straight_speed=900)
BEWEGUNGSMOTOREN.straight(-130)
BEWEGUNGSMOTOREN.arc(-100,90)
BEWEGUNGSMOTOREN.straight(30)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.straight(-200)
TOPLEFT.run_angle(1000, 162)
BEWEGUNGSMOTOREN.straight(100)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(100)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(450)
BEWEGUNGSMOTOREN.turn(95)
BEWEGUNGSMOTOREN.straight(70)
BEWEGUNGSMOTOREN.turn(-10)
TOPRIGHT.run_angle(1000,-1300)
BEWEGUNGSMOTOREN.straight(-100)
BEWEGUNGSMOTOREN.turn(-60)
BEWEGUNGSMOTOREN.straight(10000)