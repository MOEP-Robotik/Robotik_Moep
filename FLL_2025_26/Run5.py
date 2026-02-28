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
BEWEGUNGSMOTOREN.straight(190)
BEWEGUNGSMOTOREN.turn(135)
BEWEGUNGSMOTOREN.straight(-890)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(-100)
BEWEGUNGSMOTOREN.turn(-45)

BEWEGUNGSMOTOREN.straight(100)
TOPLEFT.run_angle(1000, -1000, wait=False)
wait(10)
BEWEGUNGSMOTOREN.straight(15)
wait(300)
TOPLEFT.run_angle(1000, -800)
BEWEGUNGSMOTOREN.straight(30, wait=False)
wait(30)
TOPLEFT.run_angle(1000, -400)
BEWEGUNGSMOTOREN.straight(50, wait=False)
TOPLEFT.run_angle(1000, 1000)
BEWEGUNGSMOTOREN.turn(0)#
BEWEGUNGSMOTOREN.straight(20)
TOPLEFT.run_angle(1000, 400)