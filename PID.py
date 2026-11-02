from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)

LINKS = Motor(Port.C, Direction.COUNTERCLOCKWISE)
RECHTS = Motor(Port.D)

DB = DriveBase(
    LINKS,
    RECHTS,
    62.4,  # Raddurchmesser
    104 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=500)
DB.settings(straight_acceleration=500)
DB.settings(turn_rate=800)
VORNE = Motor(port=Port.E)
HINTEN = Motor(port=Port.F)

lasterror = 0
integral = 0

def pid(messwert, sollwert, kp, kd , ki):
    global lasterror
    global integral
    abweichung = 0
    error = sollwert - messwert
    p = error*kp
    abweichung = error - lasterror
    lasterror = error
    d = abweichung * kd
    integral = 0.5 * integral + error
    i = integral * ki
    return p+d+i

settings = DB.settings()

def gyrostraight(drivebase: DriveBase, umdrehungen: int, kp: int, kd: int, ki: int):
    drivebase.reset(0)
    while drivebase.angle() < umdrehungen:
        lenkungswert = pid(HUB.imu.heading(), 0, kp, kd, ki)
        drivebase.drive(settings[0], lenkungswert)

gyrostraight(DB, 1000, 2, 40, 0.5)