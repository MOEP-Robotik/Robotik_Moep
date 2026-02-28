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
BEWEGUNGSMOTOREN.settings(turn_acceleration=100)

BEWEGUNGSMOTOREN.straight(595)
BEWEGUNGSMOTOREN.settings(straight_speed=900)
BEWEGUNGSMOTOREN.straight(-205)
BEWEGUNGSMOTOREN.arc(-100,90)
BEWEGUNGSMOTOREN.straight(10)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.settings(turn_acceleration=800)
BEWEGUNGSMOTOREN.settings(straight_speed=100)
BEWEGUNGSMOTOREN.straight(-200)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
TOPLEFT.run_angle(1000, 162)
BEWEGUNGSMOTOREN.straight(110)
BEWEGUNGSMOTOREN.turn(90)
BEWEGUNGSMOTOREN.straight(90)
BEWEGUNGSMOTOREN.turn(90)
wait(1000)
BEWEGUNGSMOTOREN.straight(405)
BEWEGUNGSMOTOREN.turn(83)
BEWEGUNGSMOTOREN.straight(92)
BEWEGUNGSMOTOREN.turn(-12)
TOPRIGHT.run_angle(1000,-1300)
BEWEGUNGSMOTOREN.straight(-100)
BEWEGUNGSMOTOREN.turn(-60)
BEWEGUNGSMOTOREN.straight(10000)