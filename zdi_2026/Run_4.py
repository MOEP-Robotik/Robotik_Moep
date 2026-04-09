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
    104 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=700)
DB.settings(turn_rate=900)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HINTEN.run_angle(1000,1)
DB.straight(200)
DB.arc(300,90)
DB.arc(-320,90)
DB.straight(140)
DB.turn(1)
DB.turn(-1)
DB.settings(straight_speed=999)
DB.straight(-50)
DB.turn(-90)
DB.settings(straight_speed=700)
DB.straight(-100)
HINTEN.run_angle(900, -550)
DB.straight(200)

