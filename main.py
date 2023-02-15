import serial
import time
#import ambient

co2 = serial.Serial('dev/ttyACM0', 115200)

co2.write('STA')
while True:
    ans = co2.read()
    print(ans)
co2.write('STP')
co2.close()