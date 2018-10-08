#!/bin/bash

# This is a test of equal temperment tuning using beep.

base_freq=440
base_note=69 #MIDI Note Number

# Give back a frequency of the note using equal temperment
# Arguments: note_number
calcFreq_ET() {
  a= $(2 ** $(expr 1 / 12))
  an= $a ** $(expr $base_note - $1)
  fn= $(expr $base_freq * $an)
  echo $fn
  return $fn
}

echo $(calcFreq_ET 81)
