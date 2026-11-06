from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait



HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)

VORNE = Motor(Port.F)
HINTEN = Motor(Port.E)

BEWEGUNGSMOTOREN.straight(-50)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.settings(turn_acceleration=200)
BEWEGUNGSMOTOREN.turn(60)
BEWEGUNGSMOTOREN.straight(-300)
BEWEGUNGSMOTOREN.settings(turn_acceleration=100)
BEWEGUNGSMOTOREN.turn(-120)
BEWEGUNGSMOTOREN.settings(turn_acceleration=200)
BEWEGUNGSMOTOREN.straight(-200)
BEWEGUNGSMOTOREN.turn(-100)
BEWEGUNGSMOTOREN.straight(-350)