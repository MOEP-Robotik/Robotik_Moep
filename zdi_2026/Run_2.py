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
    100 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=400)
DB.settings(turn_rate=700)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.turn(3)
DB.straight(530)
DB.turn(-93)
DB.straight(555)
DB.arc(-145, 90)
DB.turn(-2)
DB.straight(600)
DB.arc(150, 13)
DB.straight(200)
DB.arc(-150, 13)
DB.arc(-300, 130)
DB.straight(200)
DB.arc(-120, 45)
DB.straight(600)