import math

# middle C = 1
# add new chords here 
# values are notes of the chord given in half steps from middle C
chords = {
    "cm7":[1,4,8,11],
    "gm7":[3,6,8,11],
    "fm7":[4,6,9,13],
    "ddim":[3,6,9,12],
    "AbM7":[1,4,8,9],
    "G7":[3,6,8,12]
}

basses = {
    "cm7":1,
    "gm7":8,
    "fm7":6,
    "ddim":3,
    "AbM7":9,
    "G7":8
}

# hard-coded progression for now
progression = ["cm7", "gm7",  "cm7", "fm7",
               "cm7", "ddim", "gm7", "AbM7",
               "fm7", "gm7",  "G7",  "cm7"]

# note is distance +/- from middle C
def get_freq(note):
    return 246.96 * math.pow(2, float(note) / 12.0)


'''
example lines:
@ 48.0419 0.135061 SineEnv 0.152 256.869 0.025 0.2 0 
# SineEnv amplitude frequency attackTime releaseTime pan 
#  amplitude frequency attackTime releaseTime pan 
'''
def write_line(start, length, freq, amp, attack, release):
    line = "@ "
    line += str(start) + " "
    line += str(length) + " SineEnv "
    line += str(amp) + " "
    line += str(freq) + " "
    line += str(attack) + " "
    line += str(release) + " 0\n"
    return line

score = ""

bar_time = 1.0
# one chord per bar
for c in progression:
    # bass note 
    bass_freq = get_freq(basses[c] - 12)
    # play once per bar
    score += write_line(bar_time, 3, bass_freq, 0.2, 0.5, 1)
    # low note (mmm in mmm-pah)
    low_freq = get_freq(chords[c][0])

    # change these times to change the bassline
    for t in [0, 1.0, 2.33, 3.33]:
        score += write_line(bar_time + t, 0.3, low_freq, 0.15, 0.025, 0.2)

    # chord (pah in mmm-pah)
    for n in chords[c][1:]:
        freq = get_freq(n)
        # change these times to change when chords are played per bar
        for t in [0.5, 1.33, 1.83, 2.83, 3.5]:
            score += write_line(bar_time + t, 0.15, freq, 0.15, 0.025, 0.2)
    bar_time += 4.0

print(score)



# ignore this chunk for now 

'''
def get_m7(note):
    chord = []
    chord.append(note)
    chord.append(note + 3)
    chord.append(note + 7)
    chord.append(note + 10)
    return chord

def get_M7(note):
    chord = []
    chord.append(note)
    chord.append(note + 4)
    chord.append(note + 7)
    chord.append(note + 11)
    return chord

def get_7(note):
    chord = []
    chord.append(note)
    chord.append(note + 4)
    chord.append(note + 7)
    chord.append(note + 10)
    return chord

def get_dim7(note):
    chord = []
    chord.append(note)
    chord.append(note + 3)
    chord.append(note + 6)
    chord.append(note + 9)
    return chord

'''


