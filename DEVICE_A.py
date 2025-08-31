from DELVE import Sangam
from time import sleep
#payload System
com1 = Sangam(uart_id=0, baud_rate=9600)
com1.start()
#print("System A")
while True:
    message = "we go boom!"
    com1.send(message)
    received_message = com1.read()  
    if received_message:
        print(f"Message received: {received_message}")
    sleep(1)
