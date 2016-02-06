from skimage import io, feature, color, transform
from get_histogram import get_histogram
import matplotlib.pyplot as plt
import pickle
import sys

WIDTH, HEIGHT = (64, 64)  # 検出窓サイズ、学習画像の大きさと同じ
CELL_SIZE = 4
THRESHOLD = 3.0
HEIGHT_SIZE = int(HEIGHT / CELL_SIZE)
WIDTH_SIZE = int(WIDTH / CELL_SIZE)

svm = pickle.load(open(sys.argv[1], 'rb'))
target = color.rgb2gray(io.imread(sys.argv[2]))
target_scaled = target + 0

scale_factor = 2.0 ** (-1.0 / 8.0)
detections = []
for s in range(16):
    histogram = get_histogram(target_scaled)

    for y in range(0, histogram.shape[0] - HEIGHT_SIZE):
        for x in range(0, histogram.shape[1] - WIDTH_SIZE):
            feature = histogram[
                y:y + HEIGHT_SIZE,
                x:x + WIDTH_SIZE
            ].reshape(-1)

            score = svm.decision_function(feature)
            if score[0] > THRESHOLD:
                # 検出
                scale = (scale_factor ** s)
                detections.append({
                    'x': x * CELL_SIZE / scale,
                    'y': y * CELL_SIZE / scale,
                    'width': WIDTH / scale,
                    'height': HEIGHT / scale,
                    'score': score
                })

    target_scaled = transform.rescale(target_scaled, scale_factor)


# リスト6 Non-maximum Suppression
def overlap_score(a, b):
    left = max(a['x'], b['x'])
    right = min(a['x'] + a['width'], b['x'] + b['width'])
    top = max(a['y'], b['y'])
    bottom = min(a['x'] + a['height'], b['x'] + b['height'])
    intersect = max(0, (right - left) * (bottom - top))
    union = a['width'] * a['height'] + b['width'] * b['height'] - intersect
    return intersect / union


detections = sorted(detections, key = lambda d: d['score'], reverse = True)
print(detections)
deleted = set()

for i in range(len(detections)):
    if i in deleted: continue

    for j in range(i + 1, len(detections)):
        if overlap_score(detections[i], detections[j]) > 0.3:
            deleted.add(j)

detections = [d for i, d in enumerate(detections) if not i in deleted]

print(detections)

fig, ax1 = plt.subplots(ncols = 1, nrows = 1, figsize = (5, 3))
ax1.imshow(io.imread(sys.argv[2]))
for d in detections:
    ax1.add_patch(
        plt.Rectangle(
            (d['x'], d['y']), d['width'], d['height'],
            edgecolor = 'w', facecolor = 'none', linewidth = 2.5
        )
    )

ax1.set_title('Neko')
# ax1.axis('off')
plt.show()
