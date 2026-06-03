from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

HUB = PrimeHub()
HUB.imu.reset_heading(0)

DB = DriveBase(
    Motor(Port.D, Direction.COUNTERCLOCKWISE),
    Motor(Port.C),
    55,  # Raddurchmesser
    80  # Spurweite
)
DB.use_gyro(True)
DB.settings(straight_speed=800)
DB.settings(turn_rate=500)

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

            print(DriveBase.distance())
            DriveBase.drive((speed - pow(abs(HUB.imu.heading()), 2)) * -1, HUB.imu.heading() * verstaerkung)
    elif(distance > 0):
        while (DriveBase.distance() <= distance):
            perc = 100 - DriveBase.distance() * 100 / distance
            if(perc < 30):
                speed = max(perc * maxspeed / 100, minspeed)
                print(perc * maxspeed)

            DriveBase.drive((speed - pow(abs(HUB.imu.heading()), 2)), HUB.imu.heading()*-1 * verstaerkung)
    else:
        print("Error")

gyrostraight(DB, 3000, 3)