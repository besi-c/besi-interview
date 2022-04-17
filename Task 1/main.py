from lib import Read, Analyze
import time
import numpy

frameStreamData = [] # stream "storage"
def combineAndAnalyze(rawFrames,lastframe):
    while((lastframe+1)<len(rawFrames)): #rawFrames is the frameStream data
        frameOne= numpy.array(rawFrames[lastframe]) #get first raw frame
        frameTwo = numpy.array(rawFrames[lastframe + 1]) #get second raw frame
        combinedFrame= numpy.concatenate((frameOne,frameTwo),axis=1) #combine frames
        # My understanding I am combining two numpy objects as one array, not a python array, so Analyze is being called
        # on 1 numpy object with an array of length 20 since each small array is length 10
        Analyze(combinedFrame) #call analyze on combined frames, Analyze should append combined numpy array to "received_values"
        lastframe+=1 #move frame pointer
    return lastframe #return frame pointer

def Receiver(): #Read is sending a "stream" so a real world implementation would need a "receiver" for the data
                #Hence the creation of this function to emulate a Receiver that gets the stream data and stores it
    oneFrame = Read()
    if(oneFrame is None):
        return None
    frameStreamData.append(oneFrame)
    return frameStreamData

def main():
    # Write Code Here plus any necessary helper functions
    #at the end of .5 seconds, look at how many elements are in the array of generated values
    #take note of the very last index,
    #a frame is lastindex+1 to the whatever frame value
    #Analyze((1,2))
    #Analyze((2,3))
    #Analyze((3,4))
    #received values array should be [(1,2),(2,3),(3,4)]
    #                                  obj   obj   obj
    firstCall = time.time()
    trackFrame = 0 #frame pointer for combineAndAnalyze
    while(True):
        readData = Receiver() #Get the Data from Read
        if (readData == None):
            print("Null value returned, terminating")
            exit(-1)
        curTime = time.time() #Take note of the current time
        if((curTime-firstCall) >= 0.5): #check if .5 seconds has passed since last analysis
            #This check is slightly off because of the time it takes to run the code. There are things that could
            #be done to improve precision, but I am operating under the assumption that 0.5 seconds is any value
            # between 0.5 and 0.599... seconds
            trackFrame = combineAndAnalyze(readData,trackFrame) #Combine data in Analyze function and append it to Analyze
            #"storage". Then return the index of frameStreamData that was read last.
            #combine and analzye does the work
            firstCall = curTime
    pass
#
if __name__ == "__main__":
    main()

