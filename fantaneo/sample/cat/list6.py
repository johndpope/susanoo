# (1)
def overlap_score(a, b):
    left = max(a['x'], b['x'])
    right = min(a['x'] + a['width'], b['x'] + b['width'])
    top = max(a['y'], b['y'])
    bottom = min(a['y'] + a['height'], b['y'] + b['height'])
    intersect = max(0, (right - left) * (bottom - top))
    union = a['width'] * a['height'] + b['width'] * b['height'] - intersect
    return intersect / union
# (2)
detections = sorted(detections, key = lambda d: d['score'], reverse = True)
deleted = set()
# (3)
for i in range(len(detections)):
    if i in deleted: continue
    # (4)
    for j in range(i + 1, len(detections)):
        if overlap_score(detections[i], detections[j]) > 0.3:
            deleted.add()
detections = [d for i, d in enumerate(detections) if not i in deleted]
