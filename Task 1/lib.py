from random import randint
import numpy

# Ignore this implementation, it is simply for your testing

generated_values = []
received_values  = []

def Read():
    tmp = numpy.random.rand(1,10)
    generated_values.append(tmp)
    return tmp

def Analyze(frames):
    received_values.append(frames)