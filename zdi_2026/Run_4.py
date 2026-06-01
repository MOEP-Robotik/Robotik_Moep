##########################################
#das ist rover... soll nach Sternwarte kommen...
##########################################
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Stop
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
DB.settings(straight_speed=700, straight_acceleration=500)
DB.settings(turn_rate=600)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)


DB.straight(100)
DB.arc(-300, 90)
DB.straight(150)
DB.arc(100, 90)
DB.straight(525)
DB.straight(-450)
DB.turn(125)
DB.straight(800)
DB.turn(55)