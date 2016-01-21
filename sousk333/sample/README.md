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
  * https://github.com/t-abe/cat-face-detection/blob/master/crop_faces.py
  * 適当な風景画像をダウンロード
    * 何かまとめてダウンロードできる良いサイトはないだろうか？
  * n_negatives = int(sys.argv[3]) は負例画像数？
  

