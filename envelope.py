import numpy as np
from scipy.io import wavfile
import time
from matplotlib import pyplot
from os import path
import sine
def prepare(current, sine, wanted):
    max_samples = sine.duration * sine.sample_rate
    n = int(max_samples*wanted[0]/100)
    i = current[0]
    c = - ((current[1] - wanted[1])/(n-i+1))
    return [i, n, current[1], c]

class Envelope:
    def __init__(self, attack, decay, sustain, release):
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release


    def apply (self, sine):
        i = 1
        sine.data[0] = 0
        prepared = prepare([1, 0], sine, [self.attack[0], self.attack[1]])
        i = prepared[0]
        while (i <= prepared[1]):
            prepared[2] = prepared[2] + prepared[3]
            sine.data[i] = sine.data[i] * prepared[2]/100
            i = i + 1
        prepared = prepare([i, prepared[2]], sine, [self.decay[0], self.decay[1]])
        i = prepared[0]
        while (i <= prepared[1]):
            prepared[2] = prepared[2] + prepared[3]
            sine.data[i] = sine.data[i] * prepared[2]/100
            i = i + 1
        prepared = prepare([i, prepared[2]], sine, [self.sustain[0], self.sustain[1]])
        i = prepared[0]
        while (i <= prepared[1]):
            prepared[2] = prepared[2] + prepared[3]
            sine.data[i] = sine.data[i] * prepared[2]/100
            i = i + 1
        prepared = prepare([i, prepared[2]], sine, [self.release[0], self.release[1]])
        i = prepared[0]
        while (i <= prepared[1]):
            prepared[2] = prepared[2] + prepared[3]
            sine.data[i] = sine.data[i] * prepared[2]/100
            i = i + 1
        while (i < len(sine.data)):
            sine.data[i]=0
            i = i + 1


    def graph(self, flag=False):
        pyplot.plot(
            [0, self.attack[0], self.decay[0], self.sustain[0], self.release[0]],
            [0, self.attack[1], self.decay[1], self.sustain[1], self.release[1]]
                    )
        pyplot.axis([0, 100, 0, 100])
        pyplot.ylabel('Amplitude in %')
        pyplot.xlabel('Time in %')
        filename = path.join('output', 'envelope_graph_{}.png'.format(time.time()))
        if flag == False:
            pyplot.savefig(filename)
        else:
            pyplot.show()
        pyplot.clf()

