from machine import UART
from time import sleep

class Sangam:
 
    def __init__(self, uart_id: int, baud_rate: int = 9600, timeout: int = 1000):
        self.uart_id = uart_id
        self.baud_rate = baud_rate
        self.timeout = timeout

        # Initialize the UART serial port
        self.uart = UART(uart_id, baud_rate, timeout=timeout)

    def send(self, message: str):
        print(f'Sending message: {message}')
        message = message + '\n'
        self.uart.write(message.encode('utf-8'))

    def start(self):
        message = "Start"
        print(message)
        self.send(message)

    def read(self) -> str:
        message = self.uart.readline()
        if message:
            decoded_message = message.decode().strip()
            print(f"Message received: {decoded_message}")
            return decoded_message
        return None


if __name__ == "__main__":
    com1 = Sangam(uart_id=0, baud_rate=9600)
    com1.start()
