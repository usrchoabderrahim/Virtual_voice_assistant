#import required libraries

import sounddevice as sd
from scipy.io.wavfile import write

#sampling frequency
freq = 44100
#duration
dur = 60

#use the given values to record and audio 

recording = sd.rec(int(dur * freq),
                   samplerate=freq,
                   channels=2)

sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("first_audio.wav",freq,recording)

