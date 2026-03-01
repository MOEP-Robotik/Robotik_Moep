from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)
BEWEGUNGSMOTOREN.settings(straight_speed=800)

TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)
BEWEGUNGSMOTOREN.straight(920)
BEWEGUNGSMOTOREN.turn(40)
BEWEGUNGSMOTOREN.straight(300)
TOPRIGHT.run_angle(100, -300, wait=False)
BEWEGUNGSMOTOREN.settings(straight_speed=100)
BEWEGUNGSMOTOREN.turn(30)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.straight(-150)
BEWEGUNGSMOTOREN.turn(-65)
BEWEGUNGSMOTOREN.straight(-10000)
