# Notes from Emily O'Mahony

### Chord progression generation
This is a script for creating chord progressions with fixed time intervals in each bar and various voices for the SineEnv tutorial, found [here](https://github.com/AlloSphere-Research-Group/allolib_playground/blob/master/tutorials/synthesis/01_SineEnv.cpp). The voicings are hard-coded as is. 

If you're looking to generate your own progression, here's what to edit:
* Add chord voicings and bass notes, denoted as steps from middle C (some are there already)
* Change the progression using whatever chord names you've provided
* Change the times for bassline and chords, where each time is in seconds from the beginning of each measure, and each measure is 4 seconds long

The comments indicate for the most part where these edits should be.

[Python script for generating a chord progression](src/chords.py)



### Looping
Currently I'm working on a way to loop what's being played in the Allolib playground. Ideally this would be similar to an effects pedal, where the user could toggle on and off the recording and choose what gets looped. The time of the loop would also be variable. 

Here's a basic version of looping. A few things to know at the start: this does not support variable length notes. Rather, press 8 for short notes and 9 for long notes. You can swap between short and long at any time. More discrete lengths can be added relatively easily. 
To start looping, press 0. This will record notes played, including frequency and other preset parameters, and schedule them to be played every 8 seconds, 16 times. 

[Basic version of looping](src/loop.cpp)

Moving forward, I'd like to make this more versatile. I'd like to incorporate dynamcic scheduling so the looped notes don't have to play a fixed number of times. I'd also like to have an easier user interface for choosing layers of note sequences to play. 
