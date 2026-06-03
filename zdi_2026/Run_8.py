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
DB.settings(straight_speed=500)
DB.settings(straight_acceleration=500)
DB.settings(turn_rate=800)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.straight(300)
DB.arc(150,90)
DB.straight(390)
DB.arc(-150,90)
DB.straight(410)
DB.straight(-400)
DB.arc(-250,90)
DB.straight(-300)
HINTEN.run_angle(-1000, -500)
DB.straight(500)
DB.turn(-60)
DB.straight(1000)
