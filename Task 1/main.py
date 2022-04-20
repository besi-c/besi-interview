from lib import Read, Analyze
import time
import numpy

checkAnalyze = []
frameStreamData = [] # stream "storage"
def combineAndAnalyze(rawFrames):
    #rawFrames is an array of 2 frames
    frameOne= numpy.array(rawFrames[0]) #get first raw frame
    frameTwo = numpy.array(rawFrames[1]) #get second raw frame
    combinedFrame= numpy.concatenate((frameOne,frameTwo),axis=1) #combine frames
    # My understanding I am combining two numpy objects as one array, not a python array, so Analyze is being called
    # on 1 numpy object with an array of length 20 since each small array is length 10
    Analyze(combinedFrame) #call analyze on combined frames, Analyze should append combined numpy array to "received_values"
    checkAnalyze.append(combinedFrame)
    rawFrames.pop(0)
    return rawFrames#return array with n - 1 arrays

def Receiver(): #Read is sending a "stream" so a real world implementation would need a "receiver" for the data
                #Hence the creation of this function to emulate a Receiver that gets the stream data and stores it
    oneFrame = Read()
    if(oneFrame is None):
        return None
    frameStreamData.append(oneFrame)
    return frameStreamData

def main():
    global frameStreamData
    # Write Code Here plus any necessary helper functions
    #at the end of .5 seconds, look at how many elements are in the array of generated values
    #take note of the very last index,
    #a frame is lastindex+1 to the whatever frame value
    #Analyze((1,2))
    #Analyze((2,3))
    #Analyze((3,4))
    #received values array should be [(1,2),(2,3),(3,4)]
    #                                  obj   obj   obj
    nullVal = False
    timeStart = time.time()
    readCalls = 0#frame pointer for combineAndAnalyze
    firstRead = Receiver()
    readCalls+=1
    if(firstRead is not None):
        while(not nullVal):
            curTime = time.time() #Take note of the current time
            if((curTime-timeStart) >= 0.5): #check if .5 seconds has passed since last analysis
            #This check is slightly off because of the time it takes to run the code. There are things that could
            #be done to improve precision, but I am operating under the assumption that 0.5 seconds is any value
            # between 0.5 and 0.599... seconds
                readData = Receiver()
                readCalls += 1  #Get the Data from Read iff .5 seconds have elapsed
                if(readData is None):
                    nullVal = True
                if(readCalls>=2):
                    frameStreamData = combineAndAnalyze(readData) #Combine data in Analyze function and append it to Analyze
                 #"storage". Then return the index of frameStreamData that was read last.
                # #combine and analzye does the work
                timeStart = curTime
    pass

if __name__ == "__main__":
    main()
