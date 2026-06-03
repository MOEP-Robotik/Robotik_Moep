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

DB.straight(940)
DB.straight(-160)
DB.turn(28)
DB.settings(straight_speed=200)
DB.straight(140)
DB.settings(turn_rate=900)
DB.turn(15)
DB.settings(straight_speed=1000)
DB.arc(200, -45)
'''DB.straight(-135)
DB.turn(-45)'''
DB.straight(-850)