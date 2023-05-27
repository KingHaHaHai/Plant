import machine
from machine import ADC
import time
"""
class MG811:
    def __init__(self, pin):
        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)
        self.adc.width(ADC.WIDTH_12BIT)
        self.voltage_offset = 0
        self.ppm_offset = 0
        self.slope = 0
        self.intercept = 0

    def read(self):
        voltage = self.adc.read() / 4095 * 3.3
        ppm = self.slope * (voltage + self.voltage_offset) + self.intercept
        return ppm

    def calibrate(self, voltage_offset, ppm_offset):
        self.voltage_offset = voltage_offset
        self.ppm_offset = ppm_offset

        voltage_range = 2.8 - 0.22
        ppm_range = 5000
        self.slope = ppm_range / voltage_range

        self.intercept = self.ppm_offset - self.slope * self.voltage_offset

a = MG811(machine.Pin(32))

while True:
    print(a.read())
    time.sleep(0.1)
"""
"""
mg811 = MG811(machine.Pin(32))
voltages = []
ppms = []
for i in range(10):
    voltage = mg811.adc.read() / 4095 * 3.3
    ppm = 440# 已知浓度值
    voltages.append(voltage)
    ppms.append(ppm)
time.sleep(2)  # 等待2秒
voltage_offset = sum(voltages) / len(voltages)
ppm_offset = sum(ppms) / len(ppms)
mg811.calibrate(voltage_offset, ppm_offset)
"""


"""
a = ADC(machine.Pin(33))
b = ADC(machine.Pin(32))
while True:
    print(a.read())
    # print(b.read())
    time.sleep(0.1)
"""

import math
import machine
import time

# Hardware related macro definition.
MG_PIN = machine.Pin(33)  # define which analog input channel you are going to use
BOOL_PIN = 2
DC_GAIN = 8.5  # define the DC gain of amplifier

# Software related macro definition.
READ_SAMPLE_INTERVAL = 50
READ_SAMPLE_TIMES = 5

# Application related macro definition.
ZERO_POINT_VOLTAGE = 0.220  # define the output of the sensor in volts when the concentration of CO2 is 400PPM
REACTION_VOLTAGE = 0.020  # define the voltage drop of the sensor when move the sensor from air into 1000ppm CO2

# Globals
CO2Curve = [2.602, ZERO_POINT_VOLTAGE, (REACTION_VOLTAGE / (2.602 - 3))]
# two points are taken from the curve.
# with these two points, a line is formed which is
# "approximately equivalent" to the original curve.
# data format: {x, y, slope}; point1: (lg400, 0.324), point2: (lg4000, 0.280)
# slope = ( reaction voltage ) /(log400 –log1000)

# Initialize the serial communication.
# uart = machine.UART(0, 9600)
"""
#Set the pin mode.
bool_pin = machine.Pin(BOOL_PIN, machine.Pin.IN)
bool_pin.init(machine.Pin.IN, machine.Pin.PULL_UP)


def setup():
    global BOOL_PIN
    print("MG-811 Demostration")
"""

def loop():
    while True:
        volts = MGRead(MG_PIN)
        print("SEN-00007: ", volts, "V")

        percentage = MGGetPercentage(volts, CO2Curve)
        if percentage == -1:
            print("CO2: <400 ppm")
        else:
            print("CO2: ", percentage, "ppm")

        """
        if bool_pin.value() == 1:
            print("=====BOOL is HIGH======")
        else:
            print("=====BOOL is LOW======")
        """
        time.sleep(0.2)


def MGRead(mg_pin):
    v = 0
    for i in range(READ_SAMPLE_TIMES):
        v += machine.ADC(mg_pin).read()
        time.sleep_ms(READ_SAMPLE_INTERVAL)
    v = (v / READ_SAMPLE_TIMES) * 5 / 1024
    return v


def MGGetPercentage(volts, pcurve):
    if (volts / DC_GAIN) >= ZERO_POINT_VOLTAGE:
        return -1
    else:
        return math.pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0])
    
loop()
    
    