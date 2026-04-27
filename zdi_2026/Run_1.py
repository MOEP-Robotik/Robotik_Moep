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
DB.turn(-95)
DB.straight(550)
DB.arc(-130, 90)
DB.straight(600)
DB.turn(20)
DB.straight(120)
DB.turn(-20)
DB.straight(190)
DB.arc(-330, 60)
DB.settings(turn_rate=300)
DB.turn(-60)
DB.straight(600)
DB.turn(-50)
DB.straight(500)
"""
DB.straight(50)
DB.turn(-60)
DB.straight(450)
DB.turn(-50)
DB.straight(1100)
"""