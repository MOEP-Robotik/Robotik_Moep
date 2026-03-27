from pybricks.hubs import PrimeHub
from pybricks.tools import wait

HUB = PrimeHub()

while True:
    print(HUB.imu.heading())
    wait(500)