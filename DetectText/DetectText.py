import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np 

#Path to find image with text to read
imagePath = r'PATHTOFILE'
img = cv2.imread(imagePath)

#reader and language 
reader = easyocr.Reader(['en'])
#detect text on image
text_ = reader.readtext(img)


#to decrease invalid detections 
threshold = 0.25


for t in text_:
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, bbox[0], bbox[2], (0,255, 0), 5)
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255,0,0), 2)
#must be converted to preserve colour
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

