import board
import time
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
import pwmio

led = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0)
led2 = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
pot = AnalogIn(board.A1)

maximum = 65535
minimum = .1
rng = .45      
delay = pot.value / maximum * rng + minimum
time.sleep(delay)

while True:
    led.duty_cycle = pot.value
    led2.duty_cycle = maximum - pot.value
