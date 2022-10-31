import json
import requests
import serial
import time


# PROGRAM SETTINGS
ARDUINO_BAUDRATE = 9600  # Arduino's serial baud rate
ARDUINO_PORT = "COM4"  # where your Arduino is plugged in
DATA_DISPLAY = "ppIfMapEndsNow"  # value to send
DATA_URL = "http://localhost:20727/json"
ENABLE_FC_LED = 1  # turn on the LED if there's isn't any misses and sliderbreaks
REFRESH_TIME = 0.25  # time to wait to update displayed pp.


def parse_pp(negative_if_fc=False):
    """ Do a request to Stream companion and returns the amount of pp if maps ends now (float).
    If negative_if_fc = 1 and if the player is FCing the map, then a minus sign to the returned value is added. """

    response = requests.get(DATA_URL)  # To execute get request 

    decoded_data = response.text.encode().decode('utf-8-sig')  # fix how this is encoded
    data_json = json.loads(decoded_data)  # parse the json as dict

    pp = data_json[DATA_DISPLAY]
    is_fc = (data_json["miss"] < 1) and (data_json["sliderBreaks"] < 1)

    if negative_if_fc and is_fc:  # if FC
        pp *= -1  # make it negative

    return pp

# init arduino
arduino = serial.Serial(port=ARDUINO_PORT, baudrate=ARDUINO_BAUDRATE, timeout=0.01)

print("osu! parser is running...")

while True:
    current_pp = int(parse_pp(negative_if_fc=True))  # get pp
    arduino.write(bytes(str(current_pp) + "\n", 'utf-8'))
    # print(current_pp)
    time.sleep(REFRESH_TIME)

