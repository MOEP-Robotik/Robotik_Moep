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

DB.straight(760)
DB.turn(78)
DB.straight(150)
DB.arc(190, 145)
DB.straight(220)
DB.turn(-40)
DB.straight(200)