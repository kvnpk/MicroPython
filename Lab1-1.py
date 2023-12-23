from machine import Pin
import time
    
segments = (4, 5, 6, 7, 9, 10, 11)
digits = (12, 14, 0, 1)

pins = [
    Pin(4, Pin.OUT),
    Pin(5, Pin.OUT),
    Pin(6, Pin.OUT),
    Pin(7, Pin.OUT),
    Pin(9, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(11, Pin.OUT)
    ]

Numbers = [          #a, b, c, d, e, f, g
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

def seg():
    for i in pins:
        i.value(1)
        
seg()
while(1):
    for i in range(len(Numbers)):
        for j in range(len(pins)):
            pins[j].value(Numbers[i][j])
        time.sleep(i)

        