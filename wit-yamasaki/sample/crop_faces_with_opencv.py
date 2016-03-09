import cv2
import sys
from glob import iglob
import numpy as np

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

input_dir = sys.argv[1]
output_dir = sys.argv[2]

co = 0
for image_path in iglob('%s/*' % input_dir):
    if image_path.rfind("png") == -1 and \
        image_path.rfind("jpg") == -1 and \
        image_path.rfind("jpeg") == -1: continue
    try:
        img = cv2.imread(image_path)
        faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=10, minSize=(1, 1))
        for x,y,w,h in faces:
            co += 1
            dst = img[y:y+h, x:x+w]
            dst = cv2.resize(dst, (64, 64))
            cv2.imwrite("%s/img_%d.png" % (output_dir, co), dst)
    except:
        continue
