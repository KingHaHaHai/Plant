import machine

mpH = machine.ADC(machine.Pin(35))


temperature = 25
    
    

while 1:
    #tdsValue=(133.42*compensationVoltage*compensationVoltage*compensationVoltage - 255.86*compensationVoltage*compensationVoltage + 857.39*compensationVoltage)*0.5
    compensationCoefficient = 1.0+0.02*(temperature-25.0)
    # temperature compensation
    compensationVoltage = (mpH.read() * 3.3 / 4096.0) / compensationCoefficient
    tdsValue=(133.42*compensationVoltage*compensationVoltage*compensationVoltage - 255.86*compensationVoltage*compensationVoltage + 857.39*compensationVoltage)*0.5
    print(tdsValue)