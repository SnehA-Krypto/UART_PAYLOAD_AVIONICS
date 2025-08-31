from DELVE import Sangam
from time import sleep
#Avionics System
com1 = Sangam(uart_id=0, baud_rate=9600)
com1.start()
#print("System B")
while True:
    message = "Ignition!"
    com1.send(message)
    received_message = com1.read()  # Receive and print the message from the other device
    if received_message:
        print(f"Message received: {received_message}")
    sleep(1)
