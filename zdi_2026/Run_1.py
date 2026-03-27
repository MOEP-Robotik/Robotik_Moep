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
DB.settings(straight_speed=400)
DB.settings(turn_rate=500)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.turn(5)
DB.straight(560)
DB.turn(-100)
DB.straight(670)
DB.settings(turn_rate=100)
DB.turn(280)
DB.settings(turn_rate=500)
DB.turn(3)
DB.straight(700)
DB.turn(-15)
DB.straight(150)
HINTEN.run_angle(500, 300,wait=True)
DB.straight(200)
DB.turn(-80)
DB.straight(800)
DB.turn(-89)
DB.straight(300)