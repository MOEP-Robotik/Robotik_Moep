from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

class BOT():
    def __init__(self):
        motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        motor_right = Motor(Port.D)
        DB = DriveBase(
            motor_left, 
            motor_right, 
            62.4,
            104
            )
        DB.use_gyro(True)


def straight(richtung):
    integral = 0
    lastFehler = 0
    zeit = 1

    while True:

        fehler = richtung - HUB.imu.heading()
        integral += fehler
        integral = max(-100, min(integral, 100))
        lenkung = fehler / 1.5 + integral * 0.25 + (fehler - lastFehler) / 2
        DB.drive(300, lenkung)
        lastFehler = fehler
        print(zeit)
        wait(10)

straight(0)
