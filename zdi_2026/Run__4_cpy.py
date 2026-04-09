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

DB.straight(400)
DB.arc(100,90)
DB.straight(450)
DB.arc(-100,90)
DB.straight(420)
#DB.turn(2)
#DB.turn(-2)
DB.settings(straight_speed=999)
DB.straight(-115)
DB.turn(-90)
DB.settings(straight_speed=700)
DB.straight(-150)
HINTEN.run_angle(900, -550)
DB.straight(200)
DB.turn(-30)
DB.straight(1000)

