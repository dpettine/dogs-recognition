# dogs-recognition
This project provides an HAAR weak classifier trained to detect dog faces.
The HAAR classifier is built upon 1000+ real positive samples and 3000 negatives.
The training parameters used are:
numStages: 20 
minHitRate 0.99 
maxFalseAlarmRate 0.5 
w-h:  40-40 

the training process was solely based on official Open CV documentation.
Please refer to https://docs.opencv.org/trunk/dc/d88/tutorial_traincascade.html for the full documentation

The project also includes a simple python example of usage.
To test it just download the full package on your computer. 
Run the dogs.py script. The sample pictures in the 'pets' directory will be processed. Pictures containing a dog face will be copied in the 'rec' subfolder with the ROI (Region Of Interest) evidenced with a rectangle.
Some negative samples are included in the 'pets' dir to test the classifier robustness.

[Mar 29 2021]
added a cat HAAR weak classifier trained to detect cat faces (file name: cat_cascade_40x40_rev2.xml).
Same procedure used for dogs classifier used but with more samples here (3K positives samples, 9K negatives)

Also added last revision of my dog classifier, more accurate and with more samples (dog-cascade_40x40_rev2.xml)

You can tweak the simple script provided for dog classifier (dogs.py) to test the latest classifiers and see if they work for you.

Good luck!


