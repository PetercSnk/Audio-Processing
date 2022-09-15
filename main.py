from random import sample
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
frequency = 2
length = 1
amplitude = 1
phase = 0
period = length/frequency
x = np.linspace(0.000001, length, sample_rate)
sine = amplitude*np.sin(2*np.pi*frequency*x+phase)
sawtooth = -(2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
reverse_sawtooth = (2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
triangle = (4*amplitude/period)*np.abs(((x-period/4+phase)%period)-period/2)-amplitude
square = ""


plt.plot(x, sawtooth)
plt.show()


#sine_wave *= 32767
#sine_wave = np.int16(sine_wave)
#wavfile.write("file.wav", sample_rate, sine_wave)

class Wave:
    def __init__(self, waveform, f, l, a = 1, p = 0, sampleRate = 44100):
        self.f = f
        self.l = l
        self.a = a
        self.p = p
        self.sampleRate = sampleRate
        self.x = np.linspace(0.000001, l, sampleRate)
        self.y = self.createY(waveform)

    def createY(self, waveform):
        period = self.l/self.f
        if waveform == "sine":
            return self.a*np.sin(2*np.pi*self.f*self.x+self.p)
        elif waveform == "sawtooth":
            return -(2*self.a/np.pi)*np.arctan(1/(np.tan(self.x*np.pi/period)))
        elif waveform == "reverseSawtooth":
            return (2*self.a/np.pi)*np.arctan(1/(np.tan(self.x*np.pi/period)))
        elif waveform == "triangle":
            return (4*self.a/period)*np.abs(((self.x-period/4+self.p)%period)-period/2)-self.a
        else:
            raise TypeError("invalid waveform")
    
    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()


#if __name__ == "__main__":
#    wave = Wave("sine", 1, 1.0)
#    wave.plot()