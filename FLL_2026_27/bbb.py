
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Direction
from pybricks.tools import wait, StopWatch


class Bot:
    kp: float = 2
    kd: float = 40
    ki: float = 0.5

    HUB: PrimeHub
    DB: DriveBase

    motors: dict[str, Motor]

    color_sensors: dict[str, ColorSensor]

    def __init__(self, setting_param=[800, 300, 800, 300], gyro_use=False):
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

        self.DB.settings(
            straight_speed=setting_param[0],
            straight_acceleration=setting_param[1],
            turn_rate=setting_param[2],
            turn_acceleration=setting_param[3]
        )

        self.color_sensors = {
            "left": ColorSensor(Port.A),
            "right": ColorSensor(Port.B)
        }

    def __pid(
        self,
        messwert,
        sollwert: int,
        kp: float,
        kd: float,
        ki: float,
        lasterrorp: float = 0,
        integralp: float = 0
    ):
        error = sollwert - messwert

        p = error * kp

        abweichung = error - lasterrorp
        lasterror = error

        d = abweichung * kd

        integral = 0.5 * integralp + error
        i = integral * ki

        return {
            "lenkungswert": p + d + i,
            "lasterror": lasterror,
            "integral": integral
        }

    def gyrostraight(self, distance: int):
        self.DB.reset(0)

        werte = {
            "lenkungswert": 0,
            "lasterror": 0,
            "integral": 0
        }

        if distance < 0:
            while self.DB.distance() > distance:
                werte = self.__pid(
                    self.HUB.imu.heading(),
                    0,
                    self.kp,
                    self.kd,
                    self.ki,
                    werte["lasterror"],
                    werte["integral"]
                )

                self.DB.drive(
                    -self.DB.settings()[0],
                    -werte["lenkungswert"]
                )

        else:
            while self.DB.distance() < distance:
                werte = self.__pid(
                    self.HUB.imu.heading(),
                    0,
                    self.kp,
                    self.kd,
                    self.ki,
                    werte["lasterror"],
                    werte["integral"]
                )

                self.DB.drive(
                    self.DB.settings()[0],
                    werte["lenkungswert"]
                )

        self.DB.stop()

    def gyroturn(self, winkel: int, verstaerkung: float):
        if winkel == 0:
            return

        alte_beschleunigung = self.DB.settings()[3]

        self.DB.settings(turn_acceleration=1000)

        self.HUB.imu.reset_heading(0)

        winkel = winkel - 2 if winkel > 0 else winkel + 2

        while abs(winkel - self.HUB.imu.heading()) > 2:

            fehler = winkel - self.HUB.imu.heading()

            speed = 100 + abs(fehler) * verstaerkung

            if speed > self.DB.settings()[2]:
                speed = self.DB.settings()[2]

            self.DB.drive(
                0,
                (fehler / abs(fehler)) * speed
            )

        self.DB.stop()

        self.DB.settings(turn_acceleration=alte_beschleunigung)


if __name__ == "__main__":
    bot = Bot()

    bot.gyroturn(90, 0.6)

    wait(1000)

    bot.gyroturn(-90, 0.6)
