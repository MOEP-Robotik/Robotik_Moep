from pybricks.tools import hub_menu, wait
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction

hub = PrimeHub()

motors = {
    "L": Motor(Port.C, Direction.COUNTERCLOCKWISE),
    "R": Motor(Port.D),
    "F": Motor(Port.F),
    "B": Motor(Port.E)
}

motor_choice = hub_menu("L", "R", "F", "B")
motor = motors[motor_choice]

direction = hub_menu("+", "-")  

speed_choice = hub_menu("2", "4", "6", "8", "M")
if speed_choice == "M":
    speed_choice = 1000

speed = int(speed_choice) * 100

if direction == "-":
    speed = -1 * speed

motor.run(speed)

while True:
    wait(10)

motor.stop()