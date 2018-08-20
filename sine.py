import numpy as np
from scipy.io import wavfile
import time
from matplotlib import pyplot
from os import path
samplerate = 44100
vol = 1.0






class Sine:
    sample_rate = samplerate

    def __init__(self, frequency, volume, duration):
        self.t = np.linspace(0, duration, duration*self.sample_rate)
        data = np.sin(2 * np.pi * frequency * self.t) * volume
        self.data = data.astype(np.int16)
        self.duration = duration
        self.volume = volume



        self.frequency = frequency
        self.time = time.time()

    def wav(self):
        filename = path.join('output', 'sound_{}.wav'.format(self.time))

        wavfile.write(filename, self.sample_rate, self.data)

    def graph(self, flag=False):
        filename = path.join('output', 'sine_graph_{}.png'.format(self.time))
        pyplot.xlabel("Time")
        pyplot.plot(self.t, self.data)
        pyplot.axis([0, 1, 30000, -30000])
        if flag == False:
            pyplot.savefig(filename)
        else:
            pyplot.show()
        pyplot.clf()

    def addWave(self, wave):
        self.data = self.data + wave.data

    def harmonic(self, n, frequency = None):
        if frequency is None:
            frequency = self.frequency
        return Sine(n * frequency, self.volume / n, self.duration)
    def addHarmonic (self, n, freq = None):
        if freq is None:
            freq = self.frequency
        self.addWave(self.harmonic(n, freq))







