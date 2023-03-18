import machine
import time
import dht
import ssd1306

I2C = machine.SoftI2C(sda=machine.Pin(21),scl=machine.Pin(22))
m水位 = machine.ADC(machine.Pin(32))
m温湿 = dht.DHT11(machine.Pin(4))
mCO2 = machine.ADC(machine.Pin(34))
m显示屏 = ssd1306.SSD1306_I2C(128, 64, I2C)
mpH = machine.ADC(machine.Pin(35))


while 1:
    m温湿.measure()
    
    print(m水位.read())
    print(mCO2.read())
    t_m = m温湿.temperature()
    t_h = m温湿.humidity()
    print(t_m)
    print(t_h)
    print(mpH.read())
    m显示屏.text(str(t_m),0,0)
    m显示屏.text(str(t_h),0,10)
    m显示屏.show()
    time.sleep(3)
    