#!/bin/python3

import sys

# Calculates the time duration of a note from tempo and note length based on quantization

def usage():
  print("usage: ./calcLen.py Tempo [-t] note_length [note_length ...]")
  print("note_length is based on the amount of the note in a measure. \ni.e.: Whole Note is 1, Half note is 2, quarter note is 4, eight note is 8, etc.")
  print("-t : Truncate the ms value")

# Calculate the Duration in Milliseconds of a note
def length(dur, tempo):
  beat = (60 / tempo) * 1000
  #print("Duration:" + str(float(beat)))
  return beat / (dur / 4)
  
#Reads Command Args
def readArgs():
  tempo = 120
  truncate = False
  argnum = -1
  if len(sys.argv) <= 2:
    usage()
    return
  for arg in sys.argv:
    argnum += 1
    #print(str(argnum) + ":" + str(arg))
    #Ignore the command itself
    if argnum == 0:
      continue
    # This is a Tempo
    if argnum == 1:
      tempo = float(arg)
    else:
      if arg.find("-t") != -1:
        truncate = True
        continue
      if arg.isdigit() or arg.replace(".", "").isdigit():
        res = length(float(arg), tempo)
        if truncate:
          print("{0:.0f}".format(res))
        else:
          print("{0:.3f}".format(res))
      else:
        print("Invalid Syntax: " + arg)
        usage()
        return()

readArgs()
