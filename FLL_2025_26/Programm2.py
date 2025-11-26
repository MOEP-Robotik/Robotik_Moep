from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)
.
TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)

BEWEGUNGSMOTOREN.settings(straight_speed=800)

TOPLEFT.run_angle(1000, 120)
TOPRIGHT.run_angle(1000, 300, wait=False)
BEWEGUNGSMOTOREN.straight(350)
for i in range(0,5):
    TOPLEFT.run_angle(1200, -120)
    TOPLEFT.run_angle(1200, 120)
BEWEGUNGSMOTOREN.straight(-450)
TOPRIGHT.run_angle(1000, -300)