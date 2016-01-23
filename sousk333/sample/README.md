# サンプルについて

## 参考
[概要 — Python 3.5.1 ドキュメント](http://docs.python.jp/3.5/)  
[Google Python スタイルガイド — PyGuide - 2.29](http://works.surgo.jp/translation/pyguide.html)  
[はじめに — pep8-ja 1.0 ドキュメント](http://pep8-ja.readthedocs.org/ja/latest/)  

## 注意点
### サンプルコード（python 2 系）と python 3 系 の違いで気を付けること
  * print は () で囲む
  * map は 添え字でアクセスできないので list() で囲む
    * for in を使えばスマート
      * サンプルコードでは int にしないといけない
```python
# 以下は同じ
v = list(map(int, line.split()))
v = [int(i) for i in line.split()]
```
  * None の比較には == や != ではなく、is と is not

## 行ったこと
1. 猫画像ダウンロード
  * http://web.archive.org/web/20150703060412/ にアクセス
  * テキストボックスに http://137.189.35.203/WebUI/CatDatabase/catData.html を入力
  * part1, part2 ダウンロード
  * 解凍して出てきたフォルダ群を一つにまとめる
    * CAT_DATASET - CAT_00～06
2. 画像切り出し
  * 1でダウンロードした画像とアノーテションファイルより猫の顔部分の切り出しを行う
    * https://github.com/t-abe/cat-face-detection/blob/master/crop_faces.py
3. 負例画像の作成 
  * 適当な風景画像をダウンロード
    * 何かまとめてダウンロードできる良いサイトはないだろうか？
  * ダウンロードした画像から負例画像を作成する
    * https://github.com/t-abe/cat-face-detection/blob/master/crop_negatives.py
    * n_negatives = int(sys.argv[3]) はサンプルとして作成する負例画像数と等しい
      * 10000 ほど作っておく
4. 精査測定の為に、正/負例画像をぞれぞれ 1000 ずつほどよけておく
5. セルごとにLBP特徴量のヒストグラムを求める関数作成
  * P.163 リスト1 get_histogram
6. 正・負例それぞれの特徴量を計算、結果保存
  * P.164 リスト2 get_features
    * pickle化、非pickle化 の為には file 読み書きにはバイナリモード指定が必要
    * 2項と3項の組み合わせと、4項で実行して作成しておく
7. SVM で学習し、学習したモデルを保存する
  * P.165 リスト3
8. 学習済みモデルで測定する
  * 6で作成したテスト用の特徴量を用いて、7項で作成した学習済みモデルの制度を測定する
    * 結果は "Accuracy: 0.966750" となった

