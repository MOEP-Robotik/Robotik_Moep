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

HINTEN.run_angle(800, 50)
DB.arc(500, 90)
DB.arc(-220, 90)
DB.turn(-1 * HUB.imu.heading()) #maybe???
DB.straight(320)
DB.settings(straight_speed=900)
DB.straight(-60)
DB.settings(straight_speed=700)
DB.turn(-1 * HUB.imu.heading()) #maybe???
DB.turn(-90)
DB.straight(-150)
HINTEN.run_angle(-900, 500)
DB.straight(200)
DB.arc(-560, 90)
DB.straight(600)