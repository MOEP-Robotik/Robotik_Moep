#SILO IST KACKE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

TOPRIGHT.run_angle(1000, 300, wait=False)
BEWEGUNGSMOTOREN.straight(250)

"""for i in range(0,4):
    TOPLEFT.run_angle(770, 90)
    wait(500)
    TOPLEFT.run_angle(770, -90)"""

BEWEGUNGSMOTOREN.turn(-45)
BEWEGUNGSMOTOREN.straight(410)
BEWEGUNGSMOTOREN.turn(45)
BEWEGUNGSMOTOREN.straight(180)
TOPRIGHT.run_angle(1000, -220, wait=False)
BEWEGUNGSMOTOREN.settings(turn_rate=100)
BEWEGUNGSMOTOREN.turn(41)
BEWEGUNGSMOTOREN.settings(straight_speed=200)
BEWEGUNGSMOTOREN.straight(160)
TOPRIGHT.run_angle(1000, 250)
BEWEGUNGSMOTOREN.straight(-55)
BEWEGUNGSMOTOREN.settings(straight_speed=400)
BEWEGUNGSMOTOREN.turn(-60)
BEWEGUNGSMOTOREN.settings(straight_speed=800)
BEWEGUNGSMOTOREN.straight(-110)
BEWEGUNGSMOTOREN.turn(-69)
BEWEGUNGSMOTOREN.straight(-300)
BEWEGUNGSMOTOREN.straight(400)
BEWEGUNGSMOTOREN.turn(-105)
BEWEGUNGSMOTOREN.straight(650)