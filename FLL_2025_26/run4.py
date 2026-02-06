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
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(500)
BEWEGUNGSMOTOREN.turn(-50)
BEWEGUNGSMOTOREN.turn(50)
BEWEGUNGSMOTOREN.straight(-250)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(440)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(54.4)
TOPLEFT.run_angle(300, 220)
TOPLEFT.run_angle(1000, 80, wait=False)
BEWEGUNGSMOTOREN.settings(straight_speed=30)
BEWEGUNGSMOTOREN.straight(-6)
TOPLEFT.run_angle(100,100, wait=False)
BEWEGUNGSMOTOREN.straight(-48)
BEWEGUNGSMOTOREN.straight(10)
TOPLEFT.run_angle(1000, 100)
BEWEGUNGSMOTOREN.straight(-30)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(-2000)