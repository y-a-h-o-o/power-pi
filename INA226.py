import board
from ina219 import INA219

#replace with required values

ina = INA219(shunt_ohms=0.1, max_expected_amps = 0.6, address=0x40)

ina.configure(voltage_range=ina.RANGE_32V, gain=ina.GAIN_AUTO, bus_adc=ina.ADC_128SAMP,shunt_adc=ina.ADC_128SAMP)

#returns the power, voltage and current for future use
def get_values(): 
    return [ina.voltage(), ina.current(), ina.power()]
