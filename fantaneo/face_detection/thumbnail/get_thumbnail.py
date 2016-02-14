import sys
import cv
import glob
import os

storage = cv.CreateMemStorage()
hc = cv.Load("./haarcascade_frontalface_default.xml")

unknown_imgs = []
for path in glob.glob('input_images/*'):
    print("Detecting face on " + path)
    try:
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

        if len(faces) == 0:
            unknown_imgs.append(path)
            continue
        sub = cv.GetSubRect(img, (resx,resy,maxw,maxh))
        thumbnail = cv.CreateMat(64, 64, cv.CV_8UC3)
        cv.Resize(sub, thumbnail)
        filename = os.path.basename(path)
        # cv.SaveImage("./output_images/face_"+filename, sub)
        cv.SaveImage("./output_images/thumbnail_"+filename, thumbnail)
    except:
        print(sys.exec_info())

print("")
print "Detecting face process is successful !!"

if len(unknown_imgs) > 0:
    print("")
    print("but following images were unknown")
    for path in unknown_imgs:
        print(path)


