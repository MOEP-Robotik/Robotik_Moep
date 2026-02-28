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


BEWEGUNGSMOTOREN.straight(-340)
BEWEGUNGSMOTOREN.settings(turn_acceleration=100)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.settings(turn_acceleration=800)
BEWEGUNGSMOTOREN.straight(620)
BEWEGUNGSMOTOREN.turn(-80)
BEWEGUNGSMOTOREN.turn(80)
BEWEGUNGSMOTOREN.straight(-25)
BEWEGUNGSMOTOREN.turn(-90)
BEWEGUNGSMOTOREN.straight(520)
TOPRIGHT.run_angle(1000, -100)
wait(500)
BEWEGUNGSMOTOREN.turn(45)
BEWEGUNGSMOTOREN.settings(straight_speed=100)
BEWEGUNGSMOTOREN.straight(-260)
wait(50)
BEWEGUNGSMOTOREN.straight(60)
TOPRIGHT.run_angle(1000, 90)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(-60)
TOPLEFT.run_angle(1400, 360)
BEWEGUNGSMOTOREN.straight(-300)
BEWEGUNGSMOTOREN.turn(50)
BEWEGUNGSMOTOREN.straight(-800)