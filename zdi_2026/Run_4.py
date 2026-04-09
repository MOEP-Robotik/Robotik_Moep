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
DB.arc(150,90)
DB.straight(340)
DB.arc(-150,90)
wait(500)
DB.straight(317)
wait(100)
DB.turn(1)
DB.turn(-1)
DB.settings(straight_speed=999)
DB.straight(-75)
DB.turn(-95)
DB.settings(straight_speed=700)
DB.straight(-100)
HINTEN.run_angle(900, -550)
DB.arc(-400,45)
#DB.turn(-45)
DB.straight(600)
DB.turn(-45)
DB.straight(1000)

