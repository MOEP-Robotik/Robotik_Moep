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
    104 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=900)
DB.settings(turn_rate=1000)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.straight(200)
DB.arc(-350, 180)
DB.straight(135)
DB.arc(70, 90)
DB.straight(67)
VORNE.run_time(-1000, 1000)
wait(500)
DB.settings(straight_speed=1000, straight_acceleration=10000)
DB.straight(10, then=Stop.HOLD)
DB.settings(straight_speed=1000)
DB.straight(-50)
DB.settings(straight_speed=100)
DB.straight(-30)
VORNE.run_angle(1000, 700)
DB.settings(straight_speed=900, straight_acceleration=500)
VORNE.run_angle(1000, 300, wait=False)
DB.turn(-90)
DB.straight(-380)
DB.turn(-90)
DB.straight(-600)
