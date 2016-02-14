# 実行環境を構築する
## Git clone
```
% git clone https://github.com/mls-itoc/susanoo.git
```

## Dockerイメージを作成する
```
% cd fantaneo/face_detection
% docker build -t fantaneo/face_detection .
```

# 複数の画像から顔を抜き出して画像を作る

## 顔がある画像をinput_imagesに格納する
jpg拡張子の画像を入れる。

## Dockerコンテナを作成する
```
% docker run --rm -it -v /vagrant/susanoo/fantaneo/face_detection/thumbnail:/mls-itoc fantaneo/face_detection /bin/bash
```
## 顔抜き出しスクリプトを実行する
```
% python get_thumbnail.py
```
