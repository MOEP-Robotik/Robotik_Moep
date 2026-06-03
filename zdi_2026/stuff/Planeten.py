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
DB.settings(straight_speed=700, straight_acceleration=500)
DB.settings(turn_rate=600)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

DB.turn(5)
DB.arc(-300, 90)
DB.straight(202)
DB.arc(200, 64)
DB.straight(470)
DB.settings(straight_speed=500, straight_acceleration=200)
DB.straight(-35)

wait(500)

DB.stop()
HUB.imu.reset_heading(0)

for i in range(1,4):
    VORNE.run_angle(-1000, 370)
    DB.straight(-37) #Länge der Steins?? + Toleranz??
    VORNE.run_angle(1000, 360)
    DB.straight(-90 + (-1 * i))

VORNE.run_angle(-1000, 370)
DB.straight(-100)

DB.settings(straight_speed=700, straight_acceleration=500)

DB.turn(108)

DB.straight(550)
DB.turn(90)
DB.straight(300)
