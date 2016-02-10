pyenvでOpenCVをインストールする場合、Anacondaと呼ばれるNumPyなどのパッケージが一つにまとめたものを使用するのが良く使われているようです。  
ひとまず顔画像を収集するためにOpenCVを使用したいので、以下の環境を準備しました。

```
$ pyenv install anaconda-2.4.0
$ pyenv global anaconda-2.4.0
$ conda install -c https://conda.binstar.org/menpo opencv
```

顔認識用のデータをダウンロードします。

```
$ wget https://raw.githubusercontent.com/Itseez/opencv/master/data/haarcascades_cuda/haarcascade_frontalface_default.xml
```

haarcascades_cudaのを使用する理由は、haarcascadesのhaarcascade_frontalface_default.xmlを使用しようとすると、エラーが発生しました。  
以下のコマンドで変換します。

```
$ python get_thumbnail.py <image_path>
```
