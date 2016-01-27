import sys
import numpy as np
from skimage import io, feature

CELL_SIZE = 4
# p163より`それぞれ24、3`
LBP_POINTS = 24
LBP_RADIUS = 3

def get_histogram(image):
    # 上記LBP計算
    lbp = feature.local_binary_pattern(image, LBP_POINTS, LBP_RADIUS, 'uniform')
    # (1)
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

# (1) コマンドライン引数受け取り
image_path = sys.argv[1]
image = io.imread(image_path, as_grey = True)

histogram = get_histogram(image)
feature_vector = histogram.reshape(-1)
print(feature_vector)
