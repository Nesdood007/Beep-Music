#!/bin/bash

# Plays back a Beep Sheet

#Args: ./read.sh filename

while read f; do
  arr=($f)
  #Do the Beeping
  echo "-f ${arr[0]} -l ${arr[1]}"
  $(beep -f ${arr[0]} -l ${arr[1]})
done < $1
