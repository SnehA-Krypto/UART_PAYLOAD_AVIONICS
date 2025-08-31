import machine
from bmp280 import *
from machine import Pin, I2C, SPI, PWM
from imu import MPU6050
from utime import sleep
from math import degrees, atan2, sqrt
import sdcard
import uos
from sx127x import SX127x
from DELVE import Sangam

com1 = Sangam(uart_id=0, baud_rate=9600)
def altitude_HYP(hPa, temperature):
    temperature_k = temperature + 273.15
    pressure_ratio = 1013.25 / hPa
    h = (((pressure_ratio ** (1 / 5.257)) - 1) * temperature_k) / 0.0065
    return h

def altitude_IBF(pressure):
    pressure_ratio = pressure / 1013.25
    altitude = 44330 * (1 - (pressure_ratio ** (1 / 5.255)))
    return altitude


sclPin = Pin(3)
sdaPin = Pin(2)
i2c_object = I2C(1, scl=sclPin, sda=sdaPin, freq=100000)
bmp280_object = BMP280(i2c_object, addr=0x76, use_case=BMP280_CASE_WEATHER)
bmp280_object.power_mode = BMP280_POWER_NORMAL
bmp280_object.oversample = BMP280_OS_HIGH
bmp280_object.temp_os = BMP280_TEMP_OS_8
bmp280_object.press_os = BMP280_TEMP_OS_4
bmp280_object.standby = BMP280_STANDBY_250
bmp280_object.iir = BMP280_IIR_FILTER_2

def dataclct():
    while True:
    # BMP280 Data
        temperature = bmp280_object.temperature
        pressure_hPa = bmp280_object.pressure / 100.0
        h = altitude_HYP(pressure_hPa, temperature)
        altitude = altitude_IBF(pressure_hPa)
        received_message = com1.read()  # Receive and print the message from the other device
        if received_message:
            print(f"Message received: {received_message}")          #
        
        com1.send("Temperature: {:.2f} C".format(temperature))
        sleep(1)
        com1.send("Pressure: {:.2f} hPa".format(pressure_hPa))
        sleep(1)
        com1.send("Altitude (HYP): {:.2f} meters".format(h))
        sleep(1)
        com1.send("Altitude (IBF): {:.2f} meters".format(altitude))
        sleep(1)

dataclct()           # 
 