#!/bin/bash

echo generating...

for i in $(seq 1 50); do
  freq=$RANDOM
  len=$RANDOM
  let "freq %= 4000"
  let "len %= 250"
  echo $freq $len
done > gen.beep
