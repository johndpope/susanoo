以下のコマンドでダウンロードを実行します。

```
$ python get_google_image.py <検索キーワード>
```

コマンドを実行すると、outputディレクトリが作成されて画像がダウンロードされます。  
手元の環境で試したところ、一回の実行で459枚ダウンロードできたので、目的の人物の画像を集める場合は、検索キーワードを変更してダウンロードしてください。  
以下は例です。

```
一回目
$ python get_google_image.py 人物名

二回目
$ python get_google_image.py "人物名 ドラマ名"

必要な数になるまで実行してください。

TODO: ダウンロードする画像名が0001から順番にあげているので、実行したらoutputディレクトリの名前を変更して上書きされないようにしてください。
```