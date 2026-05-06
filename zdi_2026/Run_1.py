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
    100 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=400)
DB.settings(turn_rate=700)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.turn(3)
DB.straight(530)
DB.turn(-95)
DB.straight(550)
DB.arc(-130, 90)
DB.straight(600)
DB.turn(20)
DB.straight(130)
DB.turn(-20)
DB.straight(210)
DB.arc(-330, 40)
DB.straight(20)
DB.arc(-250, 60)
DB.settings(straight_speed=800, straight_acceleration=800, turn_rate=1000, turn_acceleration=800)
DB.arc(-230,60)
DB.arc(-600,6)
DB.straight(1000)