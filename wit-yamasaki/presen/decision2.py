def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import sys
import numpy as np
from skimage import io, feature, color
from skimage import transform
from glob import iglob
import pickle
import matplotlib.pyplot as plt
import cv2
from mylib import *


# 顔認識モデルをロード
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 各人物の認識モデルをロード
keys = ["horikita", "matsuko", "demon", "ashida", "kanna"]
models = {}
for key in keys:
    models[key] = pickle.load(open("model_%s.data" % key, "rb"))

# 顔部分の特徴抽出
targets = []
img = cv2.imread(sys.argv[1])
faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(1, 1))
for x, y, w, h in faces:
    dst = img[y:y+h, x:x+w]
    dst = cv2.resize(dst, (64, 64))
    targets.append(color.rgb2gray(dst))

# 認識
for target in targets:
    print("******************")
    feature = get_histogram(target).reshape(-1)

    max_dist = float("-inf")
    target = None
    for key in keys:
        dist = models[key].decision_function(feature)
        print(key, dist)
        if dist > max_dist:
            max_dist = dist
            target = key

    print(target)
    print(max_dist)
    plt.imshow(targets[0])
    plt.show()

