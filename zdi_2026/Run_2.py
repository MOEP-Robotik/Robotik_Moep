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
DB.settings(straight_acceleration=200)
DB.settings(turn_rate=800)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

VORNE.run_angle(1000, 1200, wait=False)
DB.turn(1)
DB.straight(800)
DB.turn(-5)
VORNE.run_angle(-1000, 1200)
DB.straight(50)
DB.turn(10)
DB.straight(-160)
DB.turn(20)
VORNE.run_angle(1000, 400)
DB.straight(180)
DB.settings(turn_rate=20)
DB.turn(50)
DB.settings(turn_rate=600)
DB.straight(300)
VORNE.run_angle(-1000, 800)
DB.turn(-45)
DB.straight(-650)
DB.turn(-45)
DB.straight(-400)

"""DB.straight(300)
DB.turn(160)
DB.straight(2000)"""