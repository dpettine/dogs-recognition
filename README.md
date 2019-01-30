# dogs-recognition
opencv HAAR cascade to detect dogs  
This project provides an HAAR weak classifier trained to detect dog faces.
The HAAR classifier is built upon 1000+ real positive samples and 3000 negatives.
The training parameters are specified here:
numStages: 20 
minHitRate 0.99 
maxFalseAlarmRate 0.5 
w-h:  40-40 

the training process was solely based on official Open CV documentation.
Please refer to https://docs.opencv.org/trunk/dc/d88/tutorial_traincascade.html for the full documentation required

The project also includes a simple python example of usage

