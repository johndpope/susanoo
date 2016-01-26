# 画像の読み書き・表示
import sys
from skimage import io
image_path = sys.argv[1]
output_path = sys.argv[2]
image = io.imread(image_path) # (1)
io.imsave(output_path, image) # (2)
io.imshow(image) # (3)
io.show()
