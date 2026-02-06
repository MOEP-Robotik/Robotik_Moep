from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color, Button
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)

TOPLEFT = Motor(Port.E)
TOPRIGHT = Motor(Port.A)

while True:
    if Button.LEFT in HUB.buttons.pressed():
        TOPLEFT.run(1000)
    elif Button.RIGHT in HUB.buttons.pressed():
        TOPLEFT.run(-1000)
    else:
        TOPLEFT.stop()