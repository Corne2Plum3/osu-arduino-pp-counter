# osu! Arduino Performance Points counter

A stupid osu! project with an Arduino board and a TM1637 4-digit display to display your PP.

![circuit_picture_small.jpg](https://github.com/Corne2Plum3/osu-arduino-pp-counter/blob/main/pictures/circuit_picture_small.jpg?raw=true)

## Story

**Corne2Plum3:** *\*clicks circles\**

**Corne2Plum3:** *I would like to see my current PP (Performance Points) while I'm clicking circles. I had a overlay in the past allowing to me to see it even with the game at fullscreen but it doesn't work anymore. I have an alternative, which consists to use my webbrowser which display my PP.*

**Corne2Plum3:** *I have an Arduino UNO R3 card and I'm bored. Why not using it?*

> You can just reduce the size of your osu! window and put the PP displayer somewhere in the screen you idiot...

**Corne2Plum3:** *No. Because I want to play fullscreen. If I reduce the windows size, the circles will be smaller. Plus it's more fun to play with fullscreen, plus it helps to train me to move my mouse faster.*

> Use your second monitor dumbass!

**Corne2Plum3:** *It's far from my vision. I have to look up to see it, which can be annoying while playing*

## To make short, what it is exactly?

In this project, the Arduino will display a number (your amount of PP) and turn on/off a LED (if you're FCing (Fumm Combo) the map or not) using information sent by your computer through serial communication.

This project is made for the video game osu! and is based on Stream Companion, the program which extract the amount of PP. To display the information, we use an Arduino board, with a TM1637 4-digit display module to show the amount of PP and a LED, "the FC led" to say if the map is being FCed (Full Combo gives a lot of PP btw).

## How does it works?

![project_explained.jpg](https://github.com/Corne2Plum3/osu-arduino-pp-counter/blob/main/pictures/project_explained.jpg?raw=true)

1. While your playing, a program called Stream companion will look at the game and will extract information from the game, such as the song you're playing, your score or your amount of PP for example. The data collected will be stored in a JSON file at http://localhost:20727/json.

2. A Python script (`osu_parser.py`) will send request to http://localhost:20727/json and get the information that we need. Then it converts the collected information to a simple number (signed integer), which will be sent to the Arduino board using the Serial communication.
    
    * The number is the amount of PP, without the decimals (e.g. `727.69 -> 727`)
    * The sign is used to tell if the map is being FCed. If it's true, the sign of the number will be negative. If not, the number is positive.

3. The Arduino board reads the Serial communication and grabs the number sent by the Python script. With this number it will control the displayer and the LED

    * The number (without the sign) is displayed on the 4-digit display.
    * If the sign of the recieved number is negative, then "the FC LED" will be turned on, else it will be turned off.

4. The Arduino board will wait until the Python script sends a new number.

## Stuff that you will need

### Hardware

* 1x [Arduino UNO R3](https://docs.arduino.cc/hardware/uno-rev3). You don't need *exactly* this model. If you have another Arduino card with at least 3 digitals, which should be all Arduino boards, it will be fine.
* 1x USB cable to link the Arduino board with a computer.
* 1x TM1637 4-digit display module *(there are pictures below in this document)*.
* 1x 220 Ohm resistor.
* 1x LED. For the color, you choose the color you like I don't give a f*ck.
* 1x Arduino breadbord and some jumpers.
* 4x female-to-male cables.


### Software

This project is intended to work on Windows only.

* [The osu! game](https://osu.ppy.sh/home) of course.
* [Stream companion](https://github.com/Piotrekol/StreamCompanion) to extract the PP value.
* [Python 3.4 or newer](https://www.python.org/downloads/).
* [PySerial library 3.5 or newer](https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0).
* [Arduino IDE](https://www.arduino.cc/en/software) or anything allowing you to compile and transfer a program to the Arduino card.
* [TM1637 library](https://www.arduino.cc/reference/en/libraries/tm1637/) to use the TM1637 4-digit display. [Tutorial to install the library](https://create.arduino.cc/projecthub/ryanchan/tm1637-digit-display-arduino-quick-tutorial-ca8a93).


## Arduino circuit

* Click [here](https://github.com/Corne2Plum3/osu-arduino-pp-counter/blob/main/pictures/schematic_circuit.png?raw=true) to see the circuit. The list of all components is written above.
* [Example of the circuit](https://github.com/Corne2Plum3/osu-arduino-pp-counter/blob/main/pictures/circuit_picture.jpg?raw=true) built IRL. (I'm sorry for the shitty quality picture). Putting the displayer cables between the LED's legs this is what I call cable management bro.

## Usage

1. Build the circuit above.

2. Plug the Arduino board to your computer and with the Arduino IDE, upload the program `arduino_displayer.ino` to the Arduino board. Note the communication port where the board is plugged in. **IMPORTANT**: keep your Arduino board plugged. [How to upload a program?](https://support.arduino.cc/hc/en-us/articles/4733418441116-Upload-a-sketch-in-Arduino-IDE)

3. Open with a text editor the program the script `osu_parser.py`, and set the value `ARDUINO_PORT` to the port where your Arduino is plugged, between "" *(for example, "COM4")*. Then, ensure that the value `ARDUINO_BAUDRATE` is set to the baud rate of your board serial communication. *(for example, for a Arduino UNO R3, it's 9600)*.

4. Be sure that your osu! game is not running. Then, launch **Stream Companion**.

5. Once Stream Companion is running, launch **osu!**.

6. Run with Python `osu_parser.py`. If *"osu! parser is running..."* is displayed, then your PP counter is ready.

7. Now move the board so the displayer and the LED can be easily seen. imo the best spot to pout the PP counter is at the top right corner of your screen, so at the same time you look at your ~~shitty~~ accuracy, you see your PP too.

![usage_picture.jpg](https://github.com/Corne2Plum3/osu-arduino-pp-counter/blob/main/pictures/usage_picture.jpg?raw=true)

## Bug and troubleshooting

Please read this if you have a problem, then if it doesn't help, open an issue.

### Nothing is being displayed on the 4-digit display, or the update rate is random...

First, be sure that your circuit is okay. Then if it's still not fixed, maybe the PP updates are too fast for your board. In this situation, open `osu_parser.py` and change the value of `REFRESH_TIME` to a higher number. It's the time between 2 updates, in seconds. For the best experience, it's recommended to use the smallest value possible. To help you finding the best value, run `data_sender_test.py` instead, which displays a counter, and try different values of `REFRESH_TIME` until it works.

### LED isn't turned on with 0 PP, even with FC...

It due to how the Full Combo is implemented and sent to the Arduino. It's a known issue but who seen a FC with 0 PP anyways.

### I finished a map, and the PP counter shows 1 PP difference with the game... Is my PP counter accurate.

Yes is it. It's just that in-game and on the website, the PP value, which is in reality a decimal number, is rounded (for example: `727.4 -> 727` ;  `727.6 -> 728`) while with the Arduino PP counter the decimals are just removed (with the previous example, `727.6 -> 727`), which explains the difference.
