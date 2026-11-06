from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction

from bot import Bot 

bot = Bot()

bot.gyrostraight(50)
bot.gyroturn(88, 0.6)
bot.gyrostraight(300)
bot.gyroturn(-120, 0.6)
# bot.gyrostraight(-200)
# bot.gyroturn(-100, 0.6)
# bot.gyrostraight(-350)