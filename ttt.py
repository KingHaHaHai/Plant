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

data = {}
_a = 0

while 1:
    if _a > 10:
        break
    vTime = time.time()
    
    m温湿.measure()
    print(vTime)
    mV水位 = m水位.read()
    print("mV水位",mV水位)
    mVCO2 = mCO2.read()
    print("mVCO2",mVCO2)
    mV温湿_温 = m温湿.temperature()
    print("mV温湿_温",mV温湿_温)
    mV温湿_湿 = m温湿.humidity()
    print("mV温湿_湿",mV温湿_湿)
    mVpH = mpH.read()
    print("mVpH",mVpH)
    
    #t_data['水位'] = mV水位
    #t_data['CO2'] = mVCO2
    #t_data['温'] = mV温湿_温
    #t_data['湿'] = mV温湿_湿
    #t_data['pH'] = mVpH
    t_data = [mV水位,mVCO2,mV温湿_温,mV温湿_湿,mVpH]
    data[str(vTime)] = t_data
    
    with open("data.json", 'wb') as f:
        f.write(str(data).replace("'",'"').replace("},","},\n").encode('utf-8'))
    
    m显示屏.text(str(mV温湿_温),0,0)
    m显示屏.text(str(mV温湿_湿),0,10)
    m显示屏.show()
    time.sleep(3)
    # _a += 1
    
    
print(str(data).replace("'",'"').encode('utf-8'))
# {"a": 123, }
    
