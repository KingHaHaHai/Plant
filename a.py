import machine
import time
import dht

d = dht.DHT11(machine.Pin(4))
while 1:
    try:
        d.measure()
        print(d.temperature()) # eg. 23 (°C)
        print(d.humidity())    # eg. 41 (% RH)
    except:
        pass