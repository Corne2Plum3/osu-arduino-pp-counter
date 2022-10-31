// Include the library:
#include <TM1637Display.h>

// Define the connections pins:
#define CLK 9
#define DIO 10
#define LED_FC_PIN 12

int pp_value = 0;

// Create display object of type TM1637Display:
TM1637Display display = TM1637Display(CLK, DIO);

int click_counter = 0;

void setup() {
  // display
  display.clear();
  display.setBrightness(1);

  // serial
  Serial.begin(9600);
  Serial.setTimeout(200);

  // LEDs
  pinMode(LED_FC_PIN, OUTPUT);
}

void loop() {
  
  // read
  while (!Serial.available());
  pp_value = Serial.readString().toInt();

  // display
  display.showNumberDec(abs(pp_value), false, 4, 0);

  // LED
  if(pp_value < 0) {  // negative pp => FC
    digitalWrite(LED_FC_PIN, HIGH);
  } else {
    digitalWrite(LED_FC_PIN, LOW);
  }

}
