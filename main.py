from random import sample
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.io import wavfile
#import librosa

"""def load_audio():
    audio_files = glob('/Repository/Audio Processing/*.wav')
    y, sr = librosa.load(audio_files[0])
    print(y, sr)
    pd.Series(y).plot(figsize = (10, 5), lw = 1)
    plt.show()"""

# add attack and delay
def createY(waveform, freq, duration, amp = 1, phase = 0, sampleRate = 44100, harmonies = 32):
    y = np.zeros(sampleRate*duration)
    x = np.linspace(0.000001, duration, sampleRate*duration)
    if waveform == "sine":
        wave = Wave(x, amp*np.sin(2*np.pi*freq*x+phase), freq, duration, amp, phase, sampleRate, 0)
        return wave
    elif waveform == "sawtooth":
        for k in range(1, harmonies):
            y += amp*np.sin(2*np.pi*freq*x*k+phase)/k
    elif waveform == "reverseSawtooth":
        for k in range(1, harmonies):
            y += amp*np.sin(2*np.pi*freq*x*k+np.pi+phase)/k
    elif waveform == "triangle":
        everyOtherOdd = False
        for k in range(1, harmonies, 2):
            if everyOtherOdd:
                y += amp*np.sin(2*np.pi*freq*x*k+np.pi+phase)/k**2
                everyOtherOdd = False
            else:
                y += amp*np.sin(2*np.pi*freq*x*k+phase)/k**2
                everyOtherOdd = True
        return y
    elif waveform == "square":
        for k in range(1, harmonies):
            y += amp*np.sin(2*np.pi*freq*x*(k*2-1)+phase)/(k*2-1)
    else:
        raise TypeError("invalid waveform")
    wave = Wave(x, y, freq, duration, amp, phase, sampleRate, harmonies)
    return wave

# add short wave to long wave with splicing [::] select start 
def add(wave1, wave2, offsetFreq1 = 0, offsetFreq2 = 0):
    wave1len = wave1.duration*wave1.sampleRate
    wave2len = wave2.duration*wave2.sampleRate
    wave3len = max([wave1len+offsetFreq1-offsetFreq2, wave2len+offsetFreq2-offsetFreq1])
    #print(wave1len+offsetFreq1-offsetFreq2, wave2len+offsetFreq2-offsetFreq1)
    np.zeros(wave3len)
    midStop = min([wave1len+offsetFreq1, wave2len+offsetFreq2])
    if offsetFreq1 < offsetFreq2:
        left = wave1.y[0:offsetFreq2-offsetFreq1]
        middle1 = wave1.y[offsetFreq2:midStop-offsetFreq1]
        middle2 = wave2.y[0:midStop-offsetFreq2]

    elif offsetFreq1 > offsetFreq2:
        left = wave2.y[0:offsetFreq1-offsetFreq2]
        middle1 = wave1.y[0:midStop-offsetFreq1]
        middle2 = wave2.y[offsetFreq1:midStop-offsetFreq2]
    else:
        left = None
    





    
    return 

    

class Wave():
    def __init__(self, x, y, freq, duration, amp, phase, sampleRate, harmonies):
        self.x = x
        self.y = y
        self.freq = freq
        self.duration = duration
        self.amp = amp
        self.phase = phase
        self.sampleRate = sampleRate
        self.harmonies = harmonies

    def values(self):
        print(self.x[0:5], self.y[0:5], self.freq, self.duration, self.amp, self.phase, self.sampleRate, self.harmonies)

    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()

    def save(self, fileName, y, sampleRate):
        y = y*32767
        y = np.int16(y)
        wavfile.write(f"{fileName}.wav", sampleRate, self.y)

if __name__ == "__main__":
    
    y1 = createY("sine", 1, 4)
    y2 = createY("sine", 1, 2)
    y3 = add(y1, y2, 0, 0)




