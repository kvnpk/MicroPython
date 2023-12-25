from machine import ADC, Pin
import time

# Define the ADC pin
adc_pin = Pin(34, Pin.IN)

# Create ADC object
adc = ADC(34)

while True:
    analog_value = adc.read()
    print("Analog Value:", analog_value)
    time.sleep(0.1)

