import machine
import time
import ssd1306
import dht

I2C = machine.I2C(sda=machine.Pin(21),scl=machine.Pin(22))
m水位 = machine.ADC(machine.Pin(34))
m温湿 = dht.DHT11(machine.Pin(2))
mCO2 = machine.ADC(machine.Pin(35))
m显示屏 = ssd1306.SSD1306_I2C(128, 64, I2C)


while 1:
    pass
    # m温湿.measure()
    # print(m温湿)
