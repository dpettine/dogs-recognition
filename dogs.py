import cv2
import os

dog_cascade = cv2.CascadeClassifier('cascade.xml')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "pets")

fileList = os.listdir(image_dir+"/rec")
for fileName in fileList:
	os.remove(image_dir+"/rec/"+fileName)

found = False
font = cv2.FONT_HERSHEY_SIMPLEX
stroke = 1

IMG_SIZE=200
IMG_MIN_SIZE=40
CASCADE_SCALE=1.1
MIN_NEIGH=3

for root, dirs, files in os.walk(image_dir):
	for file in files:
		print("filename: "+file)
		if file.endswith("png") or file.endswith("jpg"):
			source = cv2.imread(image_dir+"/"+file)
		
			if source.shape[0] > source.shape[1]:
				frame = cv2.resize(source, (int(IMG_SIZE*source.shape[1]/source.shape[0]),IMG_SIZE) , interpolation = cv2.INTER_CUBIC)
			else:
				frame = cv2.resize(source,(IMG_SIZE,int(IMG_SIZE*source.shape[0]/source.shape[1])) , interpolation = cv2.INTER_CUBIC)
				
			gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
			dogs = dog_cascade.detectMultiScale(gray, scaleFactor=CASCADE_SCALE, minNeighbors=MIN_NEIGH)

			for (x, y, w, h) in dogs:
				roi_color = frame[y:y+h, x:x+w]
				color = (255,255,255)
				cv2.putText(frame,"dog" , (x,y-10), font, 1, color, stroke, cv2.LINE_AA)
				cv2.rectangle(frame, (x, y), (x+w,y+h), color, stroke)
				found = True

			if found:
				cv2.imwrite(image_dir+"/rec/"+file, frame)	
				found = False

