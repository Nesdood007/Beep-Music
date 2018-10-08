#!/bin/python3

import sys

# Usage: convertNote.py <Note Name> <Note Octave>

# Converts a note octave and name into midi number

# Converts Note into MIDI Number
def convertNote(note, octave):
  val = -1
  adj = 0 #Adjust the Octave in some edge cases
  # Add support for a Testing "Space": note 0
  if note == "_":
    return 0
  if note == "B#":
    adj = 1
  if note == "Cb":
    adj = -1
  if note == "C" or note == "B#":
    val = 0
  if note == "C#" or note == "Db":
    val = 1
  if note == "D":
    val = 2
  if note == "D#" or note == "Eb":
    val = 3
  if note == "E" or note == "Fb":
    val = 4
  if note == "F" or note == "E#":
    val = 5
  if note == "F#" or note == "Gb":
    val = 6
  if note == "G":
    val = 7
  if note == "G#" or note == "Ab":
    val = 8
  if note == "A":
    val = 9
  if note == "A#" or note == "Bb":
    val = 10
  if note == "B" or note == "Cb":
    val = 11
    
  val += (octave + 1 + adj) * 12
  return val

def usage():
  print("Usage: ./convertNote.py <Note Name> <Octave> [next, etc...]")
  print("Note names: C, C#/Db, D, ... , A#/Bb, B, B#/C. Enharmonics are supported up to 1 half step.")
  print(" Underscore Character \"_\" is used for a space (really 0 note with very low frequency)")

#Reads Command Args
def readArgs():
  argnum = -1
  hasNote = False
  note = "X"
  if len(sys.argv) <= 2:
    usage()
    return
  for arg in sys.argv:
    argnum += 1
    #print(str(argnum) + ":" + str(arg))
    #Ignore the command itself
    if argnum == 0:
      continue
    else:
      if not hasNote:
        note = str(arg)
        hasNote = True
      else:
        hasNote = False
        val = convertNote(note, int(arg))
        if val < 0:
          print("ERR: Incorrect Value! " + note + " " + arg)
          usage()
          return
        print(val)
        
readArgs()
