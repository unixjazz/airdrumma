#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import pygame
from pygame.locals import *

#GPIO config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

#play functions
def snare_play(channel):   
   chan1.play(snare)
   time.sleep(0.01)
   print "3 \n"

def kick_play(channel):
   chan2.play(kick)
   time.sleep(0.01)
   print "5 \n"

def hihat_play(channel):
   chan3.play(hihat)
   time.sleep(0.01)
   print "7 \n"

def open_hihat_play(channel):
   chan4.play(open_hihat)
   time.sleep(0.01)
   print "11 \n"

def tom_play(channel):
   chan5.play(tom)
   time.sleep(0.01)
   print "12 \n"

def lowtom_play(channel):
   chan6.play(lowtom)
   time.sleep(0.01)
   print "13 \n"

def ride_play(channel):
   chan7.play(ride)
   time.sleep(0.01)
   print "15 \n"

def crash_play(channel):
   chan8.play(crash)
   time.sleep(0.01)
   print "16 \n"

# does what it says and debounces the button
GPIO.add_event_detect(3, GPIO.FALLING, callback=snare_play, bouncetime=120) 
GPIO.add_event_detect(5, GPIO.FALLING, callback=kick_play, bouncetime=150) 
GPIO.add_event_detect(7, GPIO.FALLING, callback=hihat_play, bouncetime=150) 
GPIO.add_event_detect(11, GPIO.FALLING, callback=open_hihat_play, bouncetime=120) 
GPIO.add_event_detect(12, GPIO.FALLING, callback=tom_play, bouncetime=120) 
GPIO.add_event_detect(13, GPIO.FALLING, callback=lowtom_play, bouncetime=120) 
GPIO.add_event_detect(15, GPIO.FALLING, callback=ride_play, bouncetime=120) 
GPIO.add_event_detect(16, GPIO.FALLING, callback=crash_play, bouncetime=120) 

while 1:
   time.sleep(0.001) 
