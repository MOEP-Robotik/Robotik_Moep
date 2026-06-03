from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

class BOT():
    def __init__(self):
        motor_left = Motor(Port.E, Direction.COUNTERCLOCKWISE)
        motor_right = Motor(Port.D)
        DB = DriveBase(
            motor_left, 
            motor_right, 
            62.4,
            104
            )
        DB.use_gyro(True)

        