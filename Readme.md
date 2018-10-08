# Beep Music Generator
This is a program that generates music using the "beep" command in Linux.

Beep is a program that sounds the PC beeper at a certain frequency and length. It is inherently monophonic, but can play many notes at a rapid rate, much like old NES/Famicom games would in order to feign having more voices available.

## Usage

1. Write the music notation in a text file (See below for details).
2. `$ ./convert.sh <music file> <beep File>`
  * This program will convert the music notation file into a file that contains frequencies and millisecond timings that beep can understand.
3. `$ ./read.sh <beep file>`
  * This will read and playback the beep file. If you so choose, the program can be modded to generate a shell script that can play back the beeps without the use of this program.

## Music Files
In the /example directory, there are some example music files. These files contain the tempo of the music, the notes to play, and the duration of each note.

In order for a file to be valid, it must meet the following requirements:

1. The tempo is listed before any notes.
2. All notes are definied in the following format:
  `<Note_Name> <Note_Octave> <Note_Duration>`
  Note Definitions are delimited by Spaces.
  Valid Notes include All normal Notes (i.e. C, C#, ..., B, C), and the Underscore "_" used as a space in the music.
  Octaves can be any number from 0 to infinity, though beep may not be capable of playing those notes.
  Note Durations can be any value from 0 to infinity. They go in inverse order in a time signature where the quarternote gets the beat, and 1 is equal to 4 quarter notes. 1 is the length of a whole note, 2 is a half note, 4 a quarter note, 8 an eighth note and so on. Decimal Values are also supported for other notes as well.
  All Note Definitions must be separated by a new line.
3. All comments are in a line started by a "#".

An Example is given below of the Super Mario Bros Theme Intro.:

```
# Super Mario Test Theme
tempo: 80
E 4 16 
E 4 8
E 4 8
C 4 16
E 4 8
G 4 8
_ 0 8
G 3 8
_ 0 8
```

This would then be rendered into a BeepFile, which contains frequencies and note lengths. Here is an example of the Mario Into shown above:

```
329.628 187.500
329.628 375.000
329.628 375.000
261.626 187.500
329.628 375.000
391.995 375.000
8.176 375.000
195.998 375.000
8.176 375.000
```

## Plans for the future
This project isn't really a priority for me right now, other than a programming exercise. I may add the ability to generate standalone shell scripts from the music files.
Also the generation tool is really slow right now.
If you find a neat use for this or a bug or whatever, let me know.
