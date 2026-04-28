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
DB.settings(straight_speed=500)
DB.settings(turn_rate=300)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

HUB.imu.reset_heading(0)

DB.turn(-52, then=Stop.HOLD)
DB.arc(370, 90)
DB.arc(320, 90)
DB.straight(120)
DB.arc(100, 90)
DB.straight(50)
DB.straight(-200)
DB.turn(80)
DB.straight(530)
DB.turn(-80)
DB.straight(360) #Diese Fahrt maybe etwas verlängern
DB.turn(90)
DB.turn(HUB.imu.heading()-308)
DB.straight(-100)
HINTEN.run_angle(800, 200)
HINTEN.run(500)
DB.straight(40)
HINTEN.stop()
HINTEN.run_angle(-1000, 200)
DB.straight(100)
DB.turn(-90)
DB.straight(170)
DB.turn(-80)
DB.straight(500)