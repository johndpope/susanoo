# 画像の表現を取得
import sys
from skimage import io
image_path = sys.argv[1]
image = io.imread(image_path) # (1)
# (1) 中心の画素(240, 180)を青にする
image[180, 240, 0:3] = [0, 0, 255]
# (2) 短形領域(20, 20) - (200, 140)を黒く塗りつぶす
image[20:140, 20:200, 0:3] = [0, 0, 0]
# (3) 短形領域(50, 200) - (430, 300)を暗くする
image[200:300, 50:430, 0:3] = image[200:300, 50:430, 0:3] * 0.5
io.imshow(image) # (3)
io.show()
