import machine
import time
import dht
import ssd1306
import utime
import network
import urequests

I2C = machine.SoftI2C(sda=machine.Pin(21),scl=machine.Pin(22))
m水位 = machine.ADC(machine.Pin(32))
m温湿 = dht.DHT11(machine.Pin(4))
mCO2 = machine.ADC(machine.Pin(34))
m显示屏 = ssd1306.SSD1306_I2C(128, 64, I2C)
mpH = machine.ADC(machine.Pin(35))

data = {}
_a = 0

# Wifi
wifi_id = "snow777"
wifi_pw = "snow123123"

sta_if = network.WLAN(network.STA_IF)
if sta_if.status() != 1010:
    sta_if.active(True)
    sta_if.connect(wifi_id,wifi_pw)
    while not sta_if.isconnected():
        pass
print("wifi已连接")


while 1:
    try:
        m温湿.measure()
        print(1)
        break
    except: pass
    finally: time.sleep(3)
time.sleep(3)


while 1:
    
        
    vTime = utime.localtime() # (YYYY,M,DD,...)
    _time = "{}{:0>2d}{:0>2d}{:0>2d}{:0>2d}{:0>2d}".format(vTime[0],vTime[1],vTime[2],vTime[3],vTime[4],vTime[5])
    m温湿.measure()
    print(_time)
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
    # data[str(_time)] = t_data 
    
    """
    with open("data.json", 'wb') as f:
        f.write(str(data).replace("'",'"').replace("},","},\n").encode('utf-8'))
    """
    
    urequests.get(f'http://maker.ifttt.com/trigger/plant_data/with/key/evkQF4nTovqng89zeqQx2v5mgj66dfxPnarYWwPFqDB?value1={_time}&value2={str(t_data)[1:-1]}')
    
    m显示屏.text(str(mV温湿_温),0,0)
    m显示屏.text(str(mV温湿_湿),0,10)
    m显示屏.show()
    del vTime,_time,mV水位,mVCO2,mV温湿_温,mV温湿_湿,mVpH,t_data
    time.sleep(3)
    # _a += 1
    # 运行 11 次后出现神秘报错 OSError: 23
    
print("完成")
# print(str(data).replace("'",'"').encode('utf-8'))