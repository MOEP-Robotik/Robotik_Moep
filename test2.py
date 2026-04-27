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
DB.settings(straight_speed=650)
DB.settings(straight_acceleration=100)
DB.settings(turn_rate=600)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

while True:
    VORNE.run_angle(-1000, 370)
    DB.straight(-48) #Länge des Steins?? + Toleranz???
    print(HUB.imu.heading())
    VORNE.run_angle(1000, 360)
    DB.straight(-88)