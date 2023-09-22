import random
from machine import Pin
from time import sleep_ms
from machine import Pin, PWM

led = Pin(2, Pin.OUT)
takki = Pin(14, Pin.IN, Pin.PULL_UP)
sensor = Pin(10, Pin.IN, Pin.PULL_UP)
speaker = PWM(Pin(12))
speaker.duty(0)

while True:
    
    random_number = random.randint(1, 6) #Generates a new random number every ms
    
    if not sensor.value(): #if magnet gets close to sensor
        sleep_ms(1000)
        if not sensor.value(): #checks whether magnet is still near sensor
            speaker.init()
            speaker.freq(1000)
            speaker.duty(1000)
            sleep_ms(100)
            speaker.duty(0)
        else:
            speaker.deinit()

    if not takki.value(): #if button is pressed
        sleep_ms(500)
        
        if random_number > 3:
            led.value(1)
            print(random_number)
        else:
            led.value(0)
            print(random_number)
