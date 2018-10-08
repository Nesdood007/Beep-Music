#!/bin/python3

import sys

# This script will calculate the frequency of a note using various tuning methods

# Parameters will be: [tuning_method] [truncate] note_number [note_number2 ...]

# Valid note_number will range from 0 to whatever, really.
# tuning methods will be optional (default to equal temperment), but will also have others in the future.
# truncate option will cut off any decimal portion for ease of use.

# Base note is A 440, which is A4.
base_freq = 440
base_note = 69
base_note_name = "A"

# Returns the Friendly name of the note
def name(note):
  toRet = ""
  n = note % 12
  if n == 0:
    toRet = "C"
  if n == 1:
    toRet = "C#/Db"
  if n == 2:
    toRet = "D"
  if n == 3:
    toRet = "D#/Eb"
  if n == 4:
    toRet = "E"
  if n == 5:
    toRet = "F"
  if n == 6:
    toRet = "F#/Gb"
  if n == 7:
    toRet = "G"
  if n == 8:
    toRet = "G#/Ab"
  if n == 9:
    toRet = "A"
  if n == 10:
    toRet = "A#/Bb"
  if n == 11:
    toRet = "B"
  return toRet

# Returns the Octave of a note
def octave(note):
  return (note // 12) - 1 #want Integer Division Here

# Calculates with Equal Temperment
def equalTemperment(note):
  a = pow(2, 1/12)
  #print(str(a) + " " + str(1/12) + " " + str(a * 12))
  return base_freq * pow(a, note - base_note)

# Returns the frequency of a note using a specified tuning method
def freq(note, tuningMethod):
  tm = tuningMethod.lower()
  if tm == "et":
    return equalTemperment(note)
  else:
    print("ERR: Unsupported!")
    return -1

#Display Help
def displayHelp():
  print("Usage: ./calcFreq.py [tuning_method] [-t (Truncate Frequency)] note_number [note_number ...]")
  print("[tuning_method] => -T:{et:just:test}")
  print("-t Truncate Frequency")
  print("Base note is " + str(base_note_name) + " where Note is " + str(base_note) + " and frequency is " + str(base_freq))
  
# Testing for Sanity
def _selfTest():
  print("Sanity Test: Note 81 should be A in Octave 5 with Frequency 880")
  testNote = 81
  print("Results: Name: " + str(name(testNote)) + " Octave: " + str(octave(testNote)) + " Frequency: " + str(freq(testNote, "et")) + " Truncated: " + str(int(freq(testNote, "et"))))

#Reads Command Args
def readArgs():
  note = ""
  tuningMethod = "et"
  truncate = False
  argnum = -1
  if len(sys.argv) <= 1:
    displayHelp()
    return
  for arg in sys.argv:
    argnum += 1
    #print(str(argnum) + ":" + str(arg))
    #Ignore the command itself
    if argnum == 0:
      continue
    # Can be either -tr or -t or a note number:
    else:
      if arg.find("-T:") != -1:
        tuningMethod = arg[3:]
      elif arg.find("-t") != -1:
        truncate = True
      # this should be a note number
      elif arg.isdigit():
        res = freq(int(arg), tuningMethod)
        if truncate == False:
          print("{0:.3f}".format(res))
        else:
          print("{0:.0f}".format(res))
      else:
        print("Invalid Syntax: " + arg)
        displayHelp()
        return()
      
# Code Here
#displayHelp()
#_selfTest()
readArgs()
