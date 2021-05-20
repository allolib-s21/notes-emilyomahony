# Notes from Emily O'Mahony

### Chord progression generation
This is a script for creating chord progressions with fixed time intervals in each bar and various voices for the SineEnv tutorial, found [here](https://github.com/AlloSphere-Research-Group/allolib_playground/blob/master/tutorials/synthesis/01_SineEnv.cpp). The voicings are hard-coded as is. 

If you're looking to generate your own progression, here's what to edit:
* Add chord voicings and bass notes, denoted as steps from middle C (some are there already)
* Change the progression using whatever chord names you've provided
* Change the times for bassline and chords, where each time is in seconds and each measure is 4 seconds long

The comments indicate for the most part where these edits should be.

[Python script for generating a chord progression](src/chords.py)



### Looping
Currently I'm working on a way to loop what's being played in the Allolib playground. Ideally this would be similar to an effects pedal, where the user could toggle on and off the recording and choose what gets looped. The time of the loop would also be variable. 

[Basic version of looping](src/my_sine.cpp)
