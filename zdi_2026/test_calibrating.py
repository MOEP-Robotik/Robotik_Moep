from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis, Stop
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)

VORNE = Motor(Port.F)
HINTEN = Motor(Port.E)

motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D)
DB = DriveBase(
    motor_left, 
    motor_right, 
    62,
    100
)

HUB.imu.reset_heading(0)

DB.use_gyro(True)
DB.settings(straight_speed=400)
DB.settings(turn_rate=800, turn_acceleration=1000)

HINTEN.run_angle(1000, 720)
