#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Wireless Inventors Kit Python Example 03Poll.py
Copyright (c) 2013 Ciseco Ltd.

Polled (or repeated) send and receive of LLAP messages


Author: Matt Lloyd

This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""
#import the PySerial library and sleep from the time library
import serial
from time import sleep
from urllib2 import urlopen

# declare to variables, holding the com port we wish to talk to and the speed
port = '/dev/ttyAMA0'
baud = 9600

host = 'http://127.0.0.1'

# open a serial connection using the variables above
ser = serial.Serial(port=port, baudrate=baud)

# wait for a moment before doing anything else
sleep(0.2)

def get(url):
  try:
    urlopen(url)
  except:
    print 'ERROR'
    flash(10)

def flash(n):
  for i in range(0,n):
    ser.write('a--D13HIGH--')
    sleep(0.1)
    ser.write('a--D13LOW---')
    sleep(0.1)

def light():
  if playing:
    ser.write('a--D06HIGH--')
  else:
    ser.write('a--D06LOW---')

playing = False

while True:
  m = ser.read(12) 
  print 'CMD: ' + str(m)
  if m == 'a--PLAY-----':
    flash(1)
    if playing:
      get(host + '/ajax/pause/')
      print 'PAUSED'
    else:
      get(host + '/ajax/play/')
      print 'PLAYING'
    playing = not playing
    light()
  elif m == 'a--STOP-----':
    flash(1)
    get(host + '/ajax/stop/')
    print 'STOP'
    playing = False
    light()
  elif m == 'a--JAZZ-----':
    flash(1)
    get(host + '/play/artist/88/')
    print 'JAZZ'
    playing = True
    light()
# close the serial port
ser.close()

# at the end of the script python automatically exits
