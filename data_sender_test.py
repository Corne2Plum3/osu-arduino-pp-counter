# Importing Libraries
import serial
import time

ARDUINO_PORT = "COM4"
ARDUINO_BAUDRATE = 9600

# Connect to arduino
arduino = serial.Serial(port=ARDUINO_PORT, baudrate=ARDUINO_BAUDRATE, timeout=0.1)

i = 0
while True:
    i += 1
    # value = write_read(str(i))
    arduino.write(bytes(str(i) + "\n", 'utf-8'))
    print(i)
    time.sleep(0.25)