import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.io import wavfile
import librosa

def load_audio():
    audio_files = glob('/Repository/Audio Processing/*.wav')
    y, sr = librosa.load(audio_files[0])
    print(y, sr)
    pd.Series(y).plot(figsize = (10, 5), lw = 1)
    plt.show()

sample_rate = 44100
frequency = 5
length = 2.0
amplitude = 1
phase = 0
period = length/frequency
x = np.linspace(0.000001, length, sample_rate)
sine = amplitude*np.sin(2*np.pi*frequency*x+phase)
sawtooth = -(2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
reverse_sawtooth = (2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
triangle = (4*amplitude/period)*np.abs(((x-period/4+phase)%period)-period/2)-amplitude


plt.plot(x, sine)
plt.show()


#sine_wave *= 32767
#sine_wave = np.int16(sine_wave)
#wavfile.write("file.wav", sample_rate, sine_wave)