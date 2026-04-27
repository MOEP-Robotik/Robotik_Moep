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
DB.settings(straight_acceleration=400)
DB.settings(turn_rate=600)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

wait(300)
DB.settings(turn_rate=400)
DB.turn(10)
DB.straight(-1010)
DB.arc(167, 189)
DB.straight(115)
DB.settings(straight_acceleration=300)
DB.settings(straight_acceleration=150)
DB.straight(-14)
for i in range(1,4):
    VORNE.run_angle(-1000, 370)
    DB.straight(-46) #Länge des Steins?? + Toleranz??+?
    VORNE.run_angle(1000, 360)
    DB.straight(-85)
DB.settings(straight_acceleration=800)
VORNE.run_angle(-1000, 370)
DB.straight(-150)
DB.turn(-80)
DB.straight(-550)
DB.turn(-90)
DB.straight(600)