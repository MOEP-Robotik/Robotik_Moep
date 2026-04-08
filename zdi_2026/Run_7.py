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
DB.settings(straight_speed=900)
DB.settings(turn_rate=1000)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.straight(200)
DB.arc(-300, 180)
#DB.straight(400)
DB.arc(100, 90)
#DB.straight(300)
#DB.arc(200,90)
DB.straight(180)
DB.turn(1)
DB.turn(-1)
DB.straight(-100)
DB.turn(90)
DB.straight(400)
DB.turn(-90)
DB.straight(600)