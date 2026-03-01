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
BEWEGUNGSMOTOREN.straight(260)
BEWEGUNGSMOTOREN.settings(turn_rate=600)
TOPRIGHT.run_angle(200, -200, wait=False)
BEWEGUNGSMOTOREN.turn(10)
wait(300)
BEWEGUNGSMOTOREN.straight(-150)
BEWEGUNGSMOTOREN.turn(-50)
BEWEGUNGSMOTOREN.straight(-10000)
