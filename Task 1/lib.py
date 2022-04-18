from random import randint
import numpy

# Ignore this implementation, it is simply for your testing

generated_values = [] #one "generated value" array is a frame. So one call to Read is one frame
received_values  = [] #this will be an array of arrays. This array of arrays
                    #should be in the order that read gives frames
def Read(): #this gives me one frame.
    tmp = numpy.random.rand(1,10)
    generated_values.append(tmp) #this places a single value into an arrray.
    return tmp

def Analyze(frames):
>>>>>>> a7786dcae0689cdb6d97bd0743aaeb7ccd336033
    received_values.append(frames)