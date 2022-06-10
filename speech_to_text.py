#!/usr/bin/env python3
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
from time import sleep

client = CloudSpeechClient()

while True:
  print("zeg eens wat leuks...")
  text = client.recognize(language_code='nl_NL')        
  sleep(2)  
  print(f'Je zei: {text}')
  #text = text.lower()
  print('--------')
        


