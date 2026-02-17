from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color, Button
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)

TOPLEFT = Motor(Port.E)
TOPRIGHT = Motor(Port.A)

BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)

BEWEGUNGSMOTOREN.straight(47)
TOPLEFT.run_angle(1000, -1000, wait=False)
wait(10)
BEWEGUNGSMOTOREN.straight(-15)
wait(300)
TOPLEFT.run_angle(1000, -900)
BEWEGUNGSMOTOREN.straight(30, wait=False)
wait(30)
TOPLEFT.run_angle(1000, -400)
BEWEGUNGSMOTOREN.straight(50, wait=False)
TOPLEFT.run_angle(1000, 500)