import numpy as np
import pickle
import sys
from glob import iglob
from skimage import io, color
from get_histogram import get_histogram


def get_features(directory):
    features = []
    for fn in iglob('%s/*.png' % directory):
        image = color.rgb2gray(io.imread(fn))
        features.append(get_histogram(image).reshape(-1))
        features.append(get_histogram(np.fliplr(image)).reshape(-1))
    return features


def main():
    positive_dir = sys.argv[1]
    negative_dir = sys.argv[2]
    positive_sample = get_features(positive_dir)
    negative_sample = get_features(negative_dir)
    n_positive = len(positive_sample)
    n_negative = len(negative_sample)

    X = np.array(positive_sample + negative_sample)
    y = np.array(
        [1 for i in range(n_positive)] +
        [0 for i in range(n_negative)]
    )

    pickle.dump((X, y), open(sys.argv[3], 'w'))


if __name__ == "__main__":
    main()
