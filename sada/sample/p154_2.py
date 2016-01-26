# 画像の表現を取得
import sys
from skimage import io
image_path = sys.argv[1]
image = io.imread(image_path) # (1)
# 本のサンプルと異なり、括弧で囲まないとSyntaxErrorが発生した。
print('(1)', type(image)) # (1) imageの型名を表示
print('(2)', image.shape) # (2) 各次元の大きさを表示
print('(3)', image[300, 400]) # (3) 座標（400, 300）の画素値を表示
