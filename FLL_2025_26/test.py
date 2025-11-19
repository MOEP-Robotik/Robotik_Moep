from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)

TOPLEFT = Motor(Port.E)
TOPRIGHT = Motor(Port.A)

TOPRIGHT.run_angle(10000, -100)
TOPRIGHT.run_angle(10000, 100)