#!/bin/bash

#This converts a Music File (text file with note, octave and duration) into a beep sequence

tempo=0

while read f; do
  if [[ $f == *"tempo:"* ]]; then
    tempo="${f/tempo:/}"
    continue
  fi
  if [[ $f == "#"* ]]; then
    continue
  fi
  arr=($f)
  #Do the Beeping
  #echo "$arr"
  note=$(python3 convertNote.py ${arr[0]} ${arr[1]})
  freq=$(python3 calcFreq.py $note)
  dur=$(python3 calcLen.py $tempo ${arr[2]})
  echo $freq $dur
done < $1 > $2
