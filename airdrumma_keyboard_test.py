#!/usr/bin/python

import sys
import os
import pygame
from pygame.locals import *

evdev = "/dev/input/event14"
f = open(evdev, 'r')
byte = []

keyboardMap = {
        29: "KEY_LEFTCTRL", # leonardo:
	63: "KEY_F5",       # pin 2 snare
        64: "KEY_F6",       #     3 kick
        65: "KEY_F7",       #     4 crash
        66: "KEY_F8",       #     5 hihat
        67: "KEY_F9",       #     6 tom 
        68: "KEY_F10",      #     7 lowtom
        87: "KEY_F11",      #     8 ride
        88: "KEY_F12"       #     9 open_hihat 
}

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

lowtom = pygame.mixer.Sound("samples/low_tom.wav")
lowtom.set_volume(1.0)

hihat = pygame.mixer.Sound("samples/hihat.wav")
hihat.set_volume(0.3)

open_hihat = pygame.mixer.Sound("samples/open_hihat.wav")
open_hihat.set_volume(0.2)

#main loop
while True:
   for bit in f.read(1):
      byte.append(ord(bit))
      if len(byte) == 8:
         if byte[2] in keyboardMap:
            if byte == [1, 0, byte[2], 0, 1, 0, 0, 0]:
               keypress = keyboardMap[byte[2]]
               if (keypress == "KEY_F5"):
                  chan1.play(snare)
               elif (keypress == "KEY_F6"):
                  chan2.play(kick)
               elif (keypress == "KEY_F7"):
                  chan3.play(crash)
               elif (keypress == "KEY_F8"):
                  chan4.play(hihat)
               elif (keypress == "KEY_F9"):
                  chan5.play(tom)
               elif (keypress == "KEY_F10"):
                  chan6.play(lowtom)
               elif (keypress == "KEY_F11"):
                  chan7.play(ride)
               elif (keypress == "KEY_F12"):
                  chan8.play(open_hihat)
         byte = []

