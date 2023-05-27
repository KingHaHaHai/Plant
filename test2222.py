import machine
from machine import ADC
import time


a = ADC(machine.Pin(32))
while True:
    print(a.read())
    # print(b.read())
    time.sleep(0.1)


    
    