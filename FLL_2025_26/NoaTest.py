from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Color
from pybricks.tools import wait

HUB = PrimeHub()

#ich glaube, es gibt auch eine Gyro_Drive_Base
BEWEGUNGSMOTOREN = DriveBase(Motor(Port.C), Motor(Port.D, Direction.COUNTERCLOCKWISE), 55, 100)

BEWEGUNGSMOTOREN.straight(200)