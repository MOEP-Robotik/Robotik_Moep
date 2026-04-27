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
DB.settings(straight_speed=700, straight_acceleration=750)
DB.settings(turn_rate=900)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

#HINTEN.run_angle(800, 50)
DB.arc(440, 90)
DB.arc(-180, 90)
#DB.turn(-1 * HUB.imu.heading()) #maybe???
DB.straight(350)
DB.settings(straight_speed=900, straight_acceleration=10000)
DB.straight(-55)
DB.settings(straight_speed=700, straight_acceleration=800)
#DB.turn(-1 * HUB.imu.heading()) #maybe???
DB.turn(-90)
DB.straight(-100)
HINTEN.run_angle(-900, 500)
DB.settings(straight_speed=800)
DB.straight(200)
DB.arc(-540, 90)
DB.straight(600)