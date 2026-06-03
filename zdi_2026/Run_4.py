##########################################
#das ist rover... soll nach Sternwarte kommen...
##########################################
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
    104 # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=500, straight_acceleration=500)
DB.settings(turn_rate=600)
VORNE = Motor(port=Port.C)
HINTEN = Motor(port=Port.D)

def gyrostraight(DriveBase: DriveBase, distance: int, verstaerkung: int = 1.5):
    DriveBase.reset(0, 0)
    HUB.imu.reset_heading(0)

    maxspeed = DriveBase.settings()[0]
    speed = DriveBase.settings()[0]
    minspeed = 100

    if(distance < 0):
        while (DriveBase.distance() >= distance):
            perc = 100 - DriveBase.distance() * 100 / distance
            if(perc < 30):
                speed = max(perc * maxspeed / 100, minspeed)

            DriveBase.drive((speed - pow(abs(HUB.imu.heading()), 2)) * -1, HUB.imu.heading() * verstaerkung)
    elif(distance > 0):
        while (DriveBase.distance() <= distance):
            perc = 100 - DriveBase.distance() * 100 / distance
            if(perc < 30):
                speed = max(perc * maxspeed / 100, minspeed)

            DriveBase.drive((speed - pow(abs(HUB.imu.heading()), 2)), HUB.imu.heading()*-1 * verstaerkung)
    else:
        print("Error")

DB.straight(60)
DB.settings(turn_rate=200)
DB.turn(-31)
gyrostraight(DB, 1050, 3)
DB.settings(turn_rate=200)
DB.turn(30)
DB.straight(50)
DB.straight(-300)
DB.turn(110)
gyrostraight(DB, 600, 2)
DB.turn(60)
DB.straight(400)