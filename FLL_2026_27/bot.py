from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch

class Bot:
    DB: DriveBase
    kp: int = 2
    kd: int = 40
    ki: int = 0.5
    lasterror = 0
    integral = 0
    motors: dict[str, Motor]
    color_sensors = {
        "left": ColorSensor,
        "right": ColorSensor
    }
    HUB: PrimeHub


    def __init__(self, setting_param = [800, 300, 800, 300], gyro_use = False):
        self.HUB = PrimeHub()
        self.HUB.imu.reset_heading(0)

        self.motors = {
            "left": Motor(Port.C, Direction.COUNTERCLOCKWISE),
            "right": Motor(Port.D),
            "front": Motor(Port.F),
            "back": Motor(Port.E)
        }
        self.DB = DriveBase(
            self.motors["left"],
            self.motors["right"],
            62.4,
            97
        )
        self.DB.use_gyro(gyro_use)
        self.DB.settings(straight_speed=setting_param[0],
                    straight_acceleration=setting_param[1],
                    turn_rate=setting_param[2],
                    turn_acceleration=setting_param[3])
        self.color_sensors = {
            "left": ColorSensor(port=Port.A),
            "right": ColorSensor(port=Port.B)
        }


    def __pid(
            self,
            messwert,
            sollwert: int,
            kp: float,
            kd :float,
            ki: float,
            lasterrorp: int = 0,
            integralp: int = 0
            ):
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

    def gyrostraight(self, distance: int):
        if distance < 0:
            self.DB.reset(0)
            werte = {"lenkungswert": 0, "lasterror": 0, "integral": 0}
            while self.DB.distance() > distance :
                werte = self.__pid(self.HUB.imu.heading(), 0, 
                                self.kp, self.kd, self.ki, werte["lasterror"], werte["integral"])
                self.DB.drive(-self.DB.settings()[0], -werte["lenkungswert"])
            self.DB.stop()
        else:
            self.DB.reset(0)
            werte = {"lenkungswert": 0, "lasterror": 0, "integral": 0}
            while self.DB.distance() < distance :
                werte = self.__pid(self.HUB.imu.heading(), 0, 
                                self.kp, self.kd, self.ki, werte["lasterror"], werte["integral"])
                self.DB.drive(self.DB.settings()[0], werte["lenkungswert"])
            self.DB.stop()

    def gyroturn(self, winkel :int, verstaerkung :float):
        self.DB.settings(turn_acceleration=1000)
        self.HUB.imu.reset_heading(0)
        winkel = winkel - 2 if winkel > 0 else winkel + 2
        while abs(winkel-self.HUB.imu.heading())>2:
            speed = 100+abs(winkel-self.HUB.imu.heading())*verstaerkung
            self.DB.drive(0, winkel/abs(winkel)*speed)
        self.DB.stop()
        self.HUB.imu.reset_heading(0)
        #steht gerade oben in der Intialisierung (muss ich noch bearbeiten)
        
if __name__ == "__main__":     
    bot = Bot()
    bot.gyroturn(90, 0.6)
    wait(1000)
    bot.gyroturn(-90, 0.6)
