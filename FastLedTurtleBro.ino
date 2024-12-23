#include <FastLED.h> // подключаем библиотеку

#define NUM_LEDS 24 // указываем количество светодиодов на ленте
#define PIN 30                    // указываем пин для подключения ленты

CRGB leds[NUM_LEDS];

void setup() {
   // основные настройки для адресной ленты
   FastLED.addLeds <WS2812, PIN, GRB>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
   FastLED.setBrightness(50);
}
//Необходимо указать количество светодиодов и пин к которому подключены светодиоды, он указан на самой плате.