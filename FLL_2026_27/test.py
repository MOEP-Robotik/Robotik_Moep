from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction

from bot import Bot 

bot = Bot()
bot.DB.settings(straight_speed=800)
bot.gyrostraight(700)
bot.gyroturn(-45, 0.6)
bot.gyrostraight(300)

bot.gyroturn(-120, 0.6)
# bot.gyrostraight(-200)
# bot.gyroturn(-100, 0.6)
# bot.gyrostraight(-350)
