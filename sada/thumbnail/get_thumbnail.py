import sys
import cv
import glob
import os

storage = cv.CreateMemStorage()
hc = cv.Load("./haarcascade_frontalface_default.xml")

for path in glob.glob('images/*'):
    img = cv.LoadImageM(path)
    faces = cv.HaarDetectObjects(img, hc, storage, 1.1, 3, 0, (0, 0))

    max=0
    maxh=0
    maxw=0
    resx=0
    resy=0

    for (x, y, w, h), n in faces:
      if max<w*h:
        maxw=w
        maxh=h
        resx=x
        resy=y
        max=w*h

    sub = cv.GetSubRect(img, (resx,resy,maxw,maxh))
    thumbnail = cv.CreateMat(64, 64, cv.CV_8UC3)
    cv.Resize(sub, thumbnail)
    filename = os.path.basename(path)
#   cv.SaveImage("./output/face_"+filename, sub)
    cv.SaveImage("./output/thumbnail_"+filename, thumbnail)
