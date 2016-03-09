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

svm = pickle.load(open(sys.argv[1], "rb"))
target = color.rgb2gray(io.imread(sys.argv[2]))
target_scaled = target + 0
scale_factor = 2.0 ** (-1.0 / 8.0)
detections = []

for s in range(32):
    histogram = get_histogram(target_scaled)
    print(histogram.shape)
    for y in range(0, 1 + histogram.shape[0] - int(HEIGHT / CELL_SIZE)):
        for x in range(0, 1 + histogram.shape[1] - int(WIDTH / CELL_SIZE)):
            feat = histogram[y:y + HEIGHT / CELL_SIZE,
                                x:x + WIDTH / CELL_SIZE].reshape(-1)
            score = svm.decision_function(feat)
            if score[0] > THRESHOLD:
                scale = (scale_factor ** s)
                detections.append({
                    'x': x * CELL_SIZE / scale,
                    'y': y * CELL_SIZE / scale,
                    'width': WIDTH / scale,
                    'height': HEIGHT / scale,
                    'score': score
                })
    target_scaled = transform.rescale(target_scaled, scale_factor)

print(len(detections))
print(detections)
plt.imshow(target)
for dt in detections:
    plt.gca().add_patch(plt.Rectangle((dt['x'], dt['y']), dt['width'], dt['height'], edgecolor='r', facecolor='none'))
plt.show()
