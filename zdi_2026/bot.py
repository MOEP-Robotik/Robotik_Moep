from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction, Axis
from pybricks.tools import wait, StopWatch

class BOT:
    __DB: DriveBase
    kp: int = 0
    kd: int = 0
    ki: int = 0
    lasterror = 0
    integral = 0
    motor_left: Motor
    motor_right: Motor
    HUB: PrimeHub
    settings: list[int]

    def __init__(self, setting_param = [800, 300, 800, 300], gyro_use = False):
        self.HUB = PrimeHub()
        self.HUB.imu.reset_heading(0)

        self.settings = setting_param
        self.motor_left = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.motor_right = Motor(Port.D)
        self.DB = DriveBase(
            self.motor_left, 
            self.motor_right, 
            62.4,
            97
        )
        self.DB.use_gyro(gyro_use)
        self.DB.settings(straight_speed=self.settings[0],
                    straight_acceleration=self.settings[1],
                    turn_rate=self.settings[2],
                    turn_acceleration=self.settings[3])


    def __pid(self, messwert, sollwert: int, kp: float, kd :float, ki: float, lasterrorp: int = 0, integralp: int = 0):
        lasterror = lasterrorp
        integral = integralp
        abweichung = 0
        error = sollwert - messwert
        p = error*kp
        abweichung = error - lasterror
        lasterror = error
        d = abweichung * kd
        integral = 0.5 * integral + error
        i = integral * ki
        return {"lenkungswert": p+d+i, "lasterror": lasterror, "integral": integral}

    def gyrostraight(self, umdrehungen: int):
        self.DB.reset(0)
        werte = {"lenkungswert": 0, "lasterror": 0, "integral": 0}
        while self.DB.angle() < umdrehungen:
            werte = self.__pid(self.HUB.imu.heading(), 0, self.kp, self.kd, self.ki, werte["lasterror"], werte["integral"])
            self.DB.drive(self.settings[0], werte["lenkungswert"])
    def gyroturn(self, winkel :int, verstaerkung :float):
        self.DB.settings(turn_acceleration=1000)
        self.HUB.imu.reset_heading(0)
        while abs(winkel-self.HUB.imu.heading())>2:
            speed = 100+abs(winkel-self.HUB.imu.heading())*verstaerkung
            self.DB.drive(0, winkel/abs(winkel)*speed)
        self.DB.stop()
        self.DB.settings(turn_acceleration=300)#steht gerade oben in der Intialisierung (muss ich noch bearbeiten)
        

        
            
bot = BOT(gyro_use=False)
#bot.gyrostraight(10)
bot.gyroturn(90, 0.6)# Verstärkung bei keinen Anbauteilen, passt noch nicht