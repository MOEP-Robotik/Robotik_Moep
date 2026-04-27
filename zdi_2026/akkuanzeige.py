from pybricks.hubs import PrimeHub


hub = PrimeHub()

hub.display.text(f'{hub.battery.voltage()/1000}V')