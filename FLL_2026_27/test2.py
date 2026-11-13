from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
from bot import Bot 

bot = Bot()
bot.DB.settings(straight_speed=800)
bot.gyrostraight(-300)
bot.DB.hold()
bot.gyroturn(45, 1)
#wait(100)
#bot.gyrostraight(-100)
#wait(100)
#bot.gyroturn(45, 0.5)