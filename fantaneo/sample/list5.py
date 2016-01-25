WIDTH, HEIGHT = (64, 64)
CELL_SIZE = 4
THRESHOLD = 3.0
# (1)
svm = pickle.load(open(sys.argv[1]))
target = color.rgb2gray(io.imread(sys.argv[2]))
target_scaled = target + 0
# (2)
scale_factor = 2.0 ** (-1.0 / 8.0)
detections = []
for s in range(16):
    # (3)
    histogram = get_histogram(target_scaled)
    # (4)
    for y in range(0, histogram.shape[0] - HEIGHT / CELL_SIZE):
        for x in range(0, histogram.shape[1] - WIDTH / CELL_SIZE):
            # (5)
            feature = histogram[y:y + HEIGHT / CELL_SIZE,
                                x:x + WIDTH / CELL_SIZE].reshape(-1)
            # (6)
            score = svm.decision_function(feature)
            if score[0] > THRESHOLD:
                # 検出!
                scale = (scale_factor ** s)
                detections.append({
                    'x': x * cell_size / scale,
                    'y': y * cell_size / scale,
                    'width': WIDTH / scale,
                    'height': HEIGHT / scale,
                    'score': score
                })
        target_scaled = transform.rescale(target_scaled, scale_factor)
