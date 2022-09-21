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

# sample_rate = 44100
# frequency = 2
# length = 1
# amplitude = 1
# phase = 0
# period = length/frequency
# x = np.linspace(0.000001, length, sample_rate*length)
# sine = amplitude*np.sin(2*np.pi*frequency*x+phase)
# sawtooth = -(2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
# reverse_sawtooth = (2*amplitude/np.pi)*np.arctan(1/(np.tan(x*np.pi/period)))
# triangle = (4*amplitude/period)*np.abs(((x-period/4+phase)%period)-period/2)-amplitude
# square = ""

#plt.plot(x, sawtooth)
#plt.show()

# x1= np.linspace(0.000001, 1, 44100)
# s1 = 1*np.sin(2*np.pi*2*x1)
# s2 = 1/2*np.sin(2*np.pi*4*x1)
# s3 = 1/3*np.sin(2*np.pi*6*x1)
# s4 = 1/4*np.sin(2*np.pi*8*x1)
# s5 = 1/5*np.sin(2*np.pi*10*x1)
# s6 = 1/6*np.sin(2*np.pi*12*x1)
# s7 = 1/7*np.sin(2*np.pi*14*x1)

# s4 = s1+s2+s3+s4+s5+s6+s7

#plt.plot(x1, s4)
#plt.show()
def add(y1, y2):
    return y1+y2

class Wave:
    def __init__(self, waveform, freq, duration, amp = 1, phase = 0, sampleRate = 44100):
        self.freq = freq
        self.duration = duration
        self.amp = amp
        self.phase = phase
        self.harmony = 32
        self.sampleRate = sampleRate
        self.x = np.linspace(0.000001, duration, sampleRate*duration)
        self.y = self.createY(waveform)

    def createY(self, waveform):
        y = np.zeros(self.sampleRate*self.duration)
        if waveform == "sine":
            return self.amp*np.sin(2*np.pi*self.freq*self.x+self.phase)
        elif waveform == "sawtooth":
            for k in range(1, self.harmony):
                y += self.amp*np.sin(2*np.pi*self.freq*self.x*k+self.phase)/k
            return y
        elif waveform == "reverseSawtooth":
            for k in range(1, self.harmony):
                y += self.amp*np.sin(2*np.pi*self.freq*self.x*k+np.pi+self.phase)/k
            return y
        elif waveform == "triangle":
            everyOtherOdd = False
            for k in range(1, self.harmony, 2):
                if everyOtherOdd:
                    y += self.amp*np.sin(2*np.pi*self.freq*self.x*k+np.pi+self.phase)/k**2
                    everyOtherOdd = False
                else:
                    y += self.amp*np.sin(2*np.pi*self.freq*self.x*k+self.phase)/k**2
                    everyOtherOdd = True
            return y
        elif waveform == "square":
            for k in range(1, self.harmony):
                y += self.amp*np.sin(2*np.pi*self.freq*self.x*(k*2-1)+self.phase)/(k*2-1)
            return y
        else:
            raise TypeError("invalid waveform")

    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()

    def save(self, fileName):
        self.y *= 32767
        self.y = np.int16(self.y)
        wavfile.write(f"{fileName}.wav", self.sampleRate, self.y)


#remove class? waveCreation which only returns y val

if __name__ == "__main__":
    wave = Wave("sine", 1, 5)
    wave2 = Wave("sine", 2, 5, phase=np.pi)
    wave.plot()
    wave2.plot()
    a = add(wave.y, wave2.y)



    #wave.save("square")