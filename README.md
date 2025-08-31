# UART_PAYLOAD_AVIONICS
 UART Communication Project – Avionics & Payload Systems

This project demonstrates serial (UART) communication between two embedded systems (e.g., ESP32, ESP8266, Raspberry Pi Pico) using a custom Python wrapper class called Sangam.
The setup simulates communication between an Avionics System (Device B) and a Payload System (Device A), exchanging messages in real time.

DELVE.py contains the Sangam class, which abstracts UART communication.

Each device imports Sangam and uses it to:

Initialize UART communication.

Send messages periodically.

Read incoming messages from the other device.

Messages flow like this:

[Device A] Payload → (MSG1) → [Device B] Avionics
[Device B] Avionics →  (MSG2)  → [Device A] Payload

🖥 Device Roles
Device A – Payload System

Sends (MSG1) every second.

Receives and prints messages from Device B.

Device B – Avionics System

Sends (MSG2) every second.

Receives and prints messages from Device A.

## Hardware Setup

Two boards (e.g., ESP32, ESP8266, or RP2040).

Connect UART pins cross-wise:

Device A TX → Device B RX

Device A RX → Device B TX

GND → GND (shared ground is mandatory).

Ensure both boards use the same baud rate (default 9600).

Example connection (ESP32):

Device A (UART0) TX (GPIO1)  → Device B (UART1) RX (GPIO9)
Device A (UART0) RX (GPIO3)  → Device B (UART1) TX (GPIO10)
Device A GND                 → Device B GND

## Usage

Upload DELVE.py to both devices.

Upload deviceA.py to the Payload board.

Upload deviceB.py to the Avionics board.

Run both scripts.

## Example Output

Device A Console

Start
Sending message: we go boom!
Message received: Ignition!


Device B Console

Start
Sending message: Ignition!
Message received: we go boom!

## Notes & Improvements

Ensure devices use different UART IDs if running on the same board.

To avoid echo messages, ignore your own transmissions when reading.

Add error handling for undecodable or corrupted messages.

Extend Sangam to support binary data, checksums, or packet-based communication.


IoT devices messaging over UART.

General embedded systems inter-board communication.
