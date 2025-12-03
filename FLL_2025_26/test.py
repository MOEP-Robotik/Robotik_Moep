from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)

TOPLEFT = Motor(Port.E)
TOPRIGHT = Motor(Port.A)

while True:
    TOPLEFT.run_angle(1200, -100)
    TOPLEFT.run_angle(1200, 100)