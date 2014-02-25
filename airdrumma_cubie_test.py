#!/usr/bin/python

import sys
import os
import time
import pygame
from pygame.locals import *

#initialize audio
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=920)

#allocate a channel per sample
chan1 = pygame.mixer.Channel(0)
chan2 = pygame.mixer.Channel(1)
chan3 = pygame.mixer.Channel(2)
chan4 = pygame.mixer.Channel(3)
chan5 = pygame.mixer.Channel(4)
chan6 = pygame.mixer.Channel(5)
chan7 = pygame.mixer.Channel(6)
chan8 = pygame.mixer.Channel(7)

#load samples
snare = pygame.mixer.Sound("samples/snare.wav")
snare.set_volume(1.0)

kick = pygame.mixer.Sound("samples/kick.wav")
kick.set_volume(1.0)

ride = pygame.mixer.Sound("samples/ride.wav")
ride.set_volume(0.3)

crash = pygame.mixer.Sound("samples/crash.wav")
crash.set_volume(0.3)

tom = pygame.mixer.Sound("samples/tom.wav")
tom.set_volume(1.0)

lowtom = pygame.mixer.Sound("samples/lowtom.wav")
lowtom.set_volume(1.0)

hihat = pygame.mixer.Sound("samples/hihat.wav")
hihat.set_volume(0.3)

open_hihat = pygame.mixer.Sound("samples/open_hihat.wav")
open_hihat.set_volume(0.2)

pd0 = open("/sys/class/gpio/gpio32_pd0/value","r")
pd1 = open("/sys/class/gpio/gpio31_pd1/value","r")
pd2 = open("/sys/class/gpio/gpio30_pd2/value","r")
pd10 = open("/sys/class/gpio/gpio38_pd10/value","r")
pd11 = open("/sys/class/gpio/gpio37_pd11/value","r")
pd12 = open("/sys/class/gpio/gpio36_pd12/value","r")
pd13 = open("/sys/class/gpio/gpio51_pd13/value","r")
pd16 = open("/sys/class/gpio/gpio48_pd16/value","r")

def pd0_readout():
   pd0.seek(0)
   pd0_value = int(pd0.read())
   return pd0_value

def pd1_readout():
   pd1.seek(0)
   pd1_value = int(pd1.read())
   return pd1_value

def pd2_readout():
   pd2.seek(0)
   pd2_value = int(pd2.read())
   return pd2_value

def pd10_readout():
   pd10.seek(0)
   pd10_value = int(pd10.read())
   return pd10_value

def pd11_readout():
   pd11.seek(0)
   pd11_value = int(pd11.read())
   return pd11_value

def pd12_readout():
   pd12.seek(0)
   pd12_value = int(pd12.read())
   return pd12_value

def pd13_readout():
   pd13.seek(0)
   pd13_value = int(pd13.read())
   return pd13_value

def pd16_readout():
   pd16.seek(0)
   pd16_value = int(pd16.read())
   return pd16_value

lastDebounceTime = 0  # the last time the output pin was toggled
debounceDelay = 300    # the debounce time; increase if the output flickers
lastButtonState_p0 = 0  # the previous reading from the input pin
buttonState_p0 = 0 

while True:
   pd0_val = pd0_readout()
   pd1_val = pd1_readout()
   pd2_val = pd2_readout() 
   pd10_val = pd10_readout()
   pd11_val = pd11_readout()
   pd12_val = pd12_readout()
   pd13_val = pd13_readout()
   pd16_val = pd16_readout()
   
   millis = int(round(time.time() * 1000))
   
   if pd0_val != lastButtonState_p0:
      lastDebounceTime = int(round(time.time() * 1000)) 
   
   if (millis - lastDebounceTime > debounceDelay): 
      if pd0_val != buttonState_p0:
         buttonState_p0 = pd0_readout
         if buttonState_p0 != 0:
            chan1.play(crash)

   lastButtonState_p0 = pd0_readout() 

