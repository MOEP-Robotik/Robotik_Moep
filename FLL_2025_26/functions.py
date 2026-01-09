from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)

BEWEGUNGSMOTOREN = DriveBase(
    Motor(Port.D, Direction.COUNTERCLOCKWISE),
    Motor(Port.C),
    56,  # Raddurchmesser
    150  # Spurweite
)
BEWEGUNGSMOTOREN.use_gyro(True)

TOPRIGHT = Motor(Port.A)
TOPLEFT = Motor(Port.E)

def linefollower(speed, verstaerkung, sollwert, sekunden, sensor: ColorSensor, drivebase: DriveBase):
    drivebase.settings(straight_speed=speed)
    stopwatch = StopWatch()
    stopwatch.reset()
    print(sensor.reflection())
    while stopwatch.time() < sekunden * 1000:
        sensorwert = sensor.reflection()
        print(sensorwert)
        lenkungswert = -(sensorwert - sollwert) * verstaerkung
        drivebase.drive(speed, lenkungswert)

# Aufruf
linefollower(300, 8, 25, 5, ColorSensor(Port.B), BEWEGUNGSMOTOREN)

