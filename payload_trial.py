import machine
from machine import Pin, I2C,Timer
from mpu6050 import init_mpu6050, get_mpu6050_data
from DELVE import Sangam
#payload System
com1 = Sangam(uart_id=0, baud_rate=9600)
import bme280  

mpu = I2C(0, scl=Pin(21), sda=Pin(20), freq=400000)
init_mpu6050(mpu)
i2c=I2C(1,sda=Pin(18), scl=Pin(19), freq=400000)
push_button = Pin(22, Pin.IN,Pin.PULL_UP)
Objectname=open("data.csv","w")
Objectname.write("TEMP,HUM,PRES,ACCX,ACCY,ACCZ,GYRX,GYRY,GYRZ\n")
Objectname.flush()
data = get_mpu6050_data(mpu)
bme = bme280.BME280(i2c=i2c)

def dataclct():
   while True:
     
         if bme.values is not None:        
          print(bme.values)
         else:
           print("Value from bme not retrieved") 
         if data is None: 
           print("Value from mpu6050 not retrieved") 
        print(bme.values)
        
        print("Temperature: {:.2f} °C".format(data['temp']))
        print("Acceleration: X: {:.2f}, Y: {:.2f}, Z: {:.2f} g".format(data['accel']['x'], data['accel']['y'], data['accel']['z']))
        print("Gyroscope: X: {:.2f}, Y: {:.2f}, Z: {:.2f} °/s".format(data['gyro']['x'],data['gyro']['y'], data['gyro']['z']))
        pattern = f"{data['temp']},{bme.values[2]},{bme.values[1]},{data['accel']['x']},{data['accel']['y']},{data['accel']['z']},{data['gyro']['x']},{data['gyro']['y']},{data['gyro']['z']}\n"
        com1.send(pattern)
        sleep(1) 
dataclct()   
