import sys
import numpy as np
from skimage import io, feature, color
from glob import iglob
import pickle

CELL_SIZE = 4
LBP_POINTS = 24
LBP_RADIUS = 3

paths = {
    "horikita": "C:\\work\\python\\images\\horikita_faces",
    "matsuko": "C:\\work\\python\\images\\matuko_faces",
    "demon": "C:\\work\\python\\images\\demon",
    "ashida": "C:\\work\\python\\images\\tensorflow_images\\aina_images",
    "kanna": "C:\\work\\python\\images\\tensorflow_images\\kanna_images",
    "negative": "C:\\work\\python\\images\\tensorflow_images\\negative_images",
}

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

def get_features(directory):
    features = []
    for fn in iglob('%s/*.*' % directory):
        if fn.rfind("png") == -1 and \
            fn.rfind("jpg") == -1 and \
            fn.rfind("jpeg") == -1: continue
        image = color.rgb2gray(io.imread(fn))
        features.append(get_histogram(image).reshape(-1))
        features.append(get_histogram(np.fliplr(image)).reshape(-1))
    return features

def main():
    for key in ["horikita", "matsuko", "demon", "aina", "kanna"]:
        if key != "matsuko": continue
        print(key)
        positive_dir = paths[key]
        negative_dir = paths["negative"]
        positive_sample = get_features(positive_dir)
        negative_sample = get_features(negative_dir)
        n_positives = len(positive_sample)
        n_negatives = len(negative_sample)
        # (2)
        X = np.array(positive_sample + negative_sample)
        # (3)
        y = np.array([1 for i in range(n_positives)] +
                     [0 for i in range(n_negatives)])
        # (4)
        pickle.dump((X, y), open("features_%s.data" % key, 'wb'))

if __name__ == "__main__":
    main()
