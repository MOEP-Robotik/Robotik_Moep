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
    90 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=400)
DB.settings(turn_rate=900)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.straight(540)
DB.turn(-100)
DB.straight(620)
DB.turn(-45)
DB.straight(50)
DB.turn(-37)
DB.straight(480)
wait(100)
DB.turn(10)
DB.straight(330)
HINTEN.run_angle(500, 550)
DB.straight(100)
DB.turn(-100)
DB.straight(600)
DB.turn(-90)
DB.straight(100)
DB.turn(2)
DB.straight(1000)
