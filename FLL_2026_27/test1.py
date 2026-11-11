from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch
from bot import Bot 

bot = Bot()

bot.DB.settings(straight_acceleration=1000)
bot.DB.settings(straight_speed=800)
bot.gyrostraight(400)
bot.DB.settings(straight_speed=300)
bot.gyrostraight(300)
bot.DB.settings(turn_rate=100, straight_speed=200)
wait(500)
bot.gyroturn(-30, 0.6)
bot.gyrostraight(40)
#print(bot.HUB.imu.reset_heading())
bot.gyroturn(-20, 0.5)

# bot.gyroturn(-120, 0.6)
# bot.gyrostraight(-200)
# bot.gyroturn(-100, 0.6)
# bot.gyrostraight(-350)