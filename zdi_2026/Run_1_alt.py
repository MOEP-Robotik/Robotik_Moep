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
DB.turn(-90)
DB.straight(370)
DB.turn(30)
DB.straight(300)
DB.turn(-28) #Die Drehung zum Teller
DB.straight(80)
HINTEN.run_angle(500, 550)
DB.turn(-10)
DB.straight(200)
DB.turn(-100)
DB.straight(600)
DB.turn(-90)
DB.straight(100)
DB.turn(2)
DB.straight(1000)
