#!/usr/bin/env python3
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts

from time import sleep
from gpiozero import LED
from aiy.pins import (PIN_A, PIN_B, PIN_C, PIN_D)

LED_ROOD = LED(PIN_A)
LED_BLAUW = LED(PIN_B)
LED_GEEL = LED(PIN_C)
LED_GROEN = LED(PIN_D)

def get_hints():
    return ('rood', 'blauw', 'geel', 'groen', 'tot ziens')

def main():
    hints = get_hints()
    client = CloudSpeechClient()

    with Board() as board:
      board.led.state = Led.BEACON_DARK
      print('Druk op de knop om te beginnen...')
      board.button.wait_for_press()
      print(f"Zeg wat ik moet doen: {', '.join(hints)}")
 
      while True:
        board.led.state = Led.ON
        text = client.recognize(language_code='nl_NL', hint_phrases=hints) 
        board.led.state = Led.PULSE_QUICK
        sleep(4)
 
        if text is None:
          print('Ik heb je niet goed verstaan.')
          print('--------')
          continue

        print(f'Je zei: {text}')
        text = text.lower()
        if 'rood' in text:
          tts.say('I will put the red light on', lang='en-GB') 
          LED_ROOD.on()


        elif 'tot ziens' in text:
          break
   
        print('--------')
  
if __name__ == '__main__':
    main()
