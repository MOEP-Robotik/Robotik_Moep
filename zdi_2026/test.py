from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)

DB = DriveBase(
    Motor(Port.E, Direction.COUNTERCLOCKWISE),
    Motor(Port.A),
    62.4,  # Raddurchmesser
    80  # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=800)
DB.settings(turn_rate=500)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.straight(300)
DB.turn(-90)

DB.straight