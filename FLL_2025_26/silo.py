from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color, Stop
from pybricks.tools import wait

HUB = PrimeHub()

HUB.imu.reset_heading(0)
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.D, Direction.COUNTERCLOCKWISE), Motor(Port.C), 56, 150)
BEWEGUNGSMOTOREN.use_gyro(True)
TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)

BEWEGUNGSMOTOREN.settings(straight_speed=800)
TOPRIGHT.run_angle(-500, 100, wait=False)
wait(100)
BEWEGUNGSMOTOREN.straight(420)

for i in range(5):
    TOPRIGHT.run_angle(1000, 82)
    TOPRIGHT.stop()
    wait(200)
    TOPRIGHT.run_angle(-1000, 82)

BEWEGUNGSMOTOREN.straight(-420)