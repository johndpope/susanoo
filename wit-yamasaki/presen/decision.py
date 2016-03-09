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

CELL_SIZE = 4
LBP_POINTS = 24
LBP_RADIUS = 3

WIDTH, HEIGHT = (64, 64)
CELL_SIZE = 4
THRESHOLD = 2.9

def get_histogram(image):
    lbp = feature.local_binary_pattern(image, LBP_POINTS, LBP_RADIUS, 'uniform')
    bins = LBP_POINTS + 2
    histogram = np.zeros(shape = (image.shape[0] / CELL_SIZE,
                                  image.shape[1] / CELL_SIZE, bins),
                         dtype = np.int)
    # (2)
    for y in range(0, image.shape[0] - CELL_SIZE, CELL_SIZE):
        for x in range(0, image.shape[1] - CELL_SIZE, CELL_SIZE):
            # (3)
            for dy in range(CELL_SIZE):
                for dx in range(CELL_SIZE):
                    # (4)
                    histogram[y / CELL_SIZE,
                              x / CELL_SIZE,
                              int(lbp[y + dy, x + dx])] += 1
    return histogram

keys = ["horikita", "matsuko", "demon", "ashida", "kanna"]
models = {}
for key in keys:
    models[key] = pickle.load(open("model_%s.data" % key, "rb"))
target = color.rgb2gray(io.imread(sys.argv[1]))
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

