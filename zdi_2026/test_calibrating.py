from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Stop
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)
LINKS = Motor(Port.E, Direction.COUNTERCLOCKWISE)
RECHTS = Motor(Port.A)

LINKS.reset_angle()
RECHTS.reset_angle()

DB = DriveBase(
    LINKS,
    RECHTS,
    62.4,  # Raddurchmesser
    100 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=400)
DB.settings(turn_rate=800, turn_acceleration=1000)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.turn(10)
wait(1000)