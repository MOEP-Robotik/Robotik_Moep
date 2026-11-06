from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction

from bbb import Bot 

bot = Bot()


bot.gyrostraight(50)
bot.DB.settings(straight_speed=800)
bot.DB.settings(turn_acceleration=200)
bot.gyroturn(60, 0.6)
bot.gyrostraight(300)
bot.DB.settings(turn_acceleration=100)
bot.gyroturn(-120, 0.6)
bot.DB.settings(turn_acceleration=200)
bot.gyrostraight(-200)
bot.gyroturn(-100, 0.6)
bot.gyrostraight(-350)

bot.DB.stop()