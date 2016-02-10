# Windows環境へのscikit-imageインストール

http://www.lfd.uci.edu/~gohlke/pythonlibs/

以下をダウンロード

- networkx-1.10-py3-none-any.whl
- scikit_image-0.11.3-cp35-none-win_amd64.whl

インストール

    $ pip install networkx-1.10-py3-none-any.whl

    $ pip install scikit_image-0.11.3-cp35-none-win_amd64.whl

# 正例データ作成方法

    $ python t_abe/crop_faces.py [オリジナル画像フォルダ] [出力フォルダ]

# 負例データ作成方法

	$ python t_abe/crop_negatives.py [オリジナル画像フォルダ] [出力フォルダ] [個数]

# サンプルソースの実行方法

1. 特徴データの作成

    $ python svm.py [正例画像のフォルダ] [負例画像のフォルダ] [出力ファイル名(特徴データ)]

2. 学習

    $ python learn.py [特徴データ] [出力ファイル名(認識モデルデータ)]

3. 認識

    $ python kensyutsu.py [認識モデルデータ] [画像]
