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

VORNE.run_angle(1000, 500, wait=False)
DB.straight(870)
VORNE.run_angle(-1000, 450)
DB.turn(5)
DB.straight(-160)
VORNE.run_angle(1000, 500)
DB.arc(50,80)
DB.straight(200)

"""DB.straight(300)
DB.turn(160)
DB.straight(2000)"""