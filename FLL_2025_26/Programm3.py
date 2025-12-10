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


BEWEGUNGSMOTOREN.straight(-350)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(660)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(-20)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(510)
TOPRIGHT.run_angle(1000, -90)
wait(200)
BEWEGUNGSMOTOREN.turn(45)
BEWEGUNGSMOTOREN.straight(-300)
wait(50)
TOPRIGHT.run_angle(1000, 90)
BEWEGUNGSMOTOREN.straight(60)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(-60)
TOPLEFT.run_angle(1000, 360)
BEWEGUNGSMOTOREN.straight(-300)
BEWEGUNGSMOTOREN.turn(50)
BEWEGUNGSMOTOREN.straight(-800)