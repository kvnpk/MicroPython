from machine import Pin
import time
p1 = Pin(14,Pin.OUT)
p2 = Pin(15,Pin.OUT)
p3 = Pin(13,Pin.OUT)
while(1):
    p1.on()
    time.sleep_ms(1000)
    p1.off()
    time.sleep_ms(1000)
    p2.on()
    time.sleep_ms(1000)
    p2.off()
    time.sleep_ms(1000)
    p3.on()
    time.sleep_ms(1000)
    p3.off()
    time.sleep_ms(1000)