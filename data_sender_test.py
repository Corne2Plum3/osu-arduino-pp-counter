# Importing Libraries
import serial
import time

ARDUINO_BAUDRATE = 9600
ARDUINO_PORT = "COM4"
REFRESH_TIME = 0.25  # time to wait to update displayed pp.

# Connect to arduino
arduino = serial.Serial(port=ARDUINO_PORT, baudrate=ARDUINO_BAUDRATE, timeout=0.1)

i = 0
while True:
    i += 1
    # value = write_read(str(i))
    arduino.write(bytes(str(i) + "\n", 'utf-8'))
    print(i)
    time.sleep(REFRESH_TIME)