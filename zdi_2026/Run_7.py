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
    100 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=500)
DB.settings(turn_rate=300)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.turn(-52, then=Stop.HOLD)
DB.arc(370, 90)
DB.arc(320, 90)
DB.straight(90)
DB.arc(100, 90)
DB.straight(50)
DB.straight(-200)
DB.settings(straight_speed=900, straight_acceleration=800)
DB.turn(80)
DB.straight(510)
DB.turn(-80)
DB.straight(490) #Diese Fahrt maybe etwas verlängern
DB.turn(-85)
DB.straight(500)