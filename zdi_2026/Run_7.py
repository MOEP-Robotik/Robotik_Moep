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
DB.straight(325)
DB.arc(-150,90)
DB.straight(380)
DB.straight(-370)
DB.arc(-250,90)
DB.settings(straight_speed=200, straight_acceleration=200)
DB.straight(-340)
DB.settings(straight_speed=600, straight_acceleration=500)
HINTEN.run_angle(-1000, 300)
DB.straight(450)
DB.turn(-65)
DB.straight(1000)
