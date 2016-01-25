CELL_SIZE = 4
def get_histogram(image):
    lbp = # 上記LBP計算
    # (1)
    bins = LBP_POINT + 2
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
