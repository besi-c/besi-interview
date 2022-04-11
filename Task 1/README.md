# Data Analysis

You are provided 2 functions,

Read and Analayze,
The Read function provides you a new numpy array of data we'll call a frame
The Analyze function takes a combined frame of data in the correct order it was received.
ie) If you receive frame 1 then frame 2, analyze frame 12, and then receive frame 3, analzye frame 23, etc.

The point of this task to run the Analyze function on 
a continuous stream of data provided by the Read function

## Task Overview
While Read provides non-null data, read data every 0.5 seconds and Analyze the data.