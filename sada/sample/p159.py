import sys
import numpy as np
from skimage import io
# transformをimportしないとエラーが発生する
from skimage import transform
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# (省略) リスト1と同様にimport

def compute_score_map(template, target):
    # (2) 拡大縮小しない場合と同じ方法でscore_mapを計算
    th, tw = template.shape
    score_map = np.zeros(shape = (target.shape[0] - th,
                                  target.shape[1] - tw))
    for y in range(score_map.shape[0]):
        for x in range(score_map.shape[1]):
            diff = target[y:y + th, x:x + tw] - template
            score_map[y, x] = np.square(diff).sum()
    return score_map

def main():
    # (1) コマンドライン引数受け取り
    template_path = sys.argv[1]
    target_path = sys.argv[2]

    # (2) テンプレート、対象画像の読み込み(グレースケール)
    template = io.imread(template_path, as_grey = True)
    target = io.imread(target_path, as_grey = True)
    th, tw = template.shape

    # (1) 画像を 2^1/8 ずつ縮小しながら各スケールのscore_mapを計算
    score_maps = []
    scale_factor = 2.0 ** (-1.0 / 8.0)
    target_scaled = target + 0
    for s in range(8):
        score_maps.append(compute_score_map(template, target_scaled))
        target_scaled = transform.rescale(target_scaled, scale_factor)

    # (3) SSDが最小のスケール、座標を取得
    score, s, (x, y) = min([(np.min(score_map), s,
                             np.unravel_index(np.argmin(score_map), score_map.shape))
                             for s, score_map in enumerate(score_maps)])

    # (4) 結果を可視化
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 3))
    ax1.imshow(template, cmap=cm.Greys_r)
    ax1.set_axis_off()
    ax1.set_title('template')
    ax2.imshow(target, cmap=cm.Greys_r)
    ax2.set_axis_off()
    ax2.set_title('target')
    scale = (scale_factor ** s)
    th, tw = template.shape
    rect = plt.Rectangle((y / scale, x / scale), tw / scale, th / scale,
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)
    plt.show()

if __name__ == "__main__":
    main()
