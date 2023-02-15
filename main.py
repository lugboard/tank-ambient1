import serial
import time
#import ambient

co2 = serial.Serial('/dev/ttyACM0', 115200)

co2.write(b'STA')
print('send STA')
out = co2.readline() #prevent error
out = co2.readline()
#print(ans.decode())
co2.write(b'STP')
room_env = out.decode().strip().split(',')
print(room_env)
print('send STP')
co2.close()