インターネット上の機械学習をやってみるとのことでしたので、以下のURL先の記事をやってみました。

[画風を変換するアルゴリズム](https://research.preferred.jp/2015/09/chainer-gogh/)

### Deep Learningについて

データサイエンティスト養成読本のp68に概要が書いてありました。

### Caffeについて

データサイエンティスト養成読本のp70に概要が書いてありました。

Caffeを使うことで自分で作成したデータセットを学習させることができるようです。

### Chainerについて

データサイエンティスト養成読本のp70に概要が書いてありました。

ChainerはCaffeの学習済みのモデルを読み込み使用することができる機能があります。

### chainer-goghによる画風の変換

画像を好きな画風に変換できるプログラムの [chainer-gogh](https://github.com/mattya/chainer-gogh) を使用しました。

chainer-goghをPython 3で使用しようとするとエラーが発生しました。
printメソッドの括弧などの細かい部分を対応しても以下のエラーが発生します。

```
$ python chainer-gogh.py -m nin -i sample_images/cat.png -s sample_images/style_0.png -o /tmp -g -1
load model... nin_imagenet.caffemodel
Traceback (most recent call last):
  File "chainer-gogh.py", line 183, in <module>
    nn = NIN()
  File "/home/sada/repos/chainer-gogh/models.py", line 12, in __init__
    self.model = caffe.CaffeFunction(fn)
  File "/home/sada/.anyenv/envs/pyenv/versions/3.5.1/lib/python3.5/site-packages
/chainer/links/caffe/caffe_function.py", line 105, in __init__
    raise RuntimeError('CaffeFunction is not supported on Python 3')
RuntimeError: CaffeFunction is not supported on Python 3
```

上記のエラーメッセージを基に検索したところ、以下のURL先のドキュメントがヒットしました。

[Caffe Reference Model Support](http://docs.chainer.org/en/stable/reference/caffe.html)

ChainerのCaffeFunctionがPython 3に未対応なのでエラーが発生するようでした。

```
This class only supports Python 2.7, since the compiled module for protocol buffers only supports Python 2. The __init__ function raises an exception in Python 3.
```

上記のように非対応のため、Python 2でインストールし直しました。
インターネット上にあるPythonのサンプルコードは、Python 2を想定しているコードが検索時にヒットすることが多いので、Python 2の環境を準備する方が機械学習に集中できそうだからです。

以下はPython 2をインストールした時の作業したコマンドです。

```
$ pyenv install 2.7.11
$ pyenv global 2.7.11

$ pip install numpy
$ pip install scipy
$ pip install matplotlib
$ pip install scikit-learn
$ pip install pillow
```

[Chainer](https://github.com/pfnet/chainer) のREADMEに書いてあったHDF5の準備です。
HDF5を使用しないので必要なかったかもしれません。

```
$ sudo apt-get install libhdf5-dev
$ pip install cython
$ pip install h5py
```

chainer-goghのREADMEを参考に画像の画風を変換しました。

```
$ pip install chainer
$ git clone https://github.com/mattya/chainer-gogh.git
$ cd chainer-gogh
```

Caffeの学習済みモデルをダウンロードします。

```
$ wget https://www.dropbox.com/s/0cidxafrb2wuwxw/nin_imagenet.caffemodel
$ mkdir cats
```

以下を実行すると完了するまでにとても時間が掛かります。

```
$ python chainer-gogh.py -m nin -i sample_images/cat.png -s sample_images/style_0.png -o cats -g -1
```


chainer-gogh.pyの以下によるとデフォルトで5000回繰り返して完了するようです。

```
parser.add_argument('--iter', default=5000, type=int,
                    help='number of iteration')
```

### 用語

CUDA(Compute Unified Device Architecture: クーダ)

> NVIDIAが提供するGPU向けのC言語の統合開発環境であり、コンパイラ(nvcc)やライブラリなどから構成されている。

Deep LearningのインストールのドキュメントにCUDAを使用するか書かれていることがあります。
CUDAの設定をするということは、Deep LearningでGPUを使用してできるようにするということのようです。

Graphics Processing Unit(GPU: グラフィックス プロセッシング ユニット)

> パーソナルコンピュータやワークステーション等の画像処理を担当する主要な部品のひとつ

HDF5(Hierarchical Data Format 5)

> 科学技術計算などの分野で、たとえば時系列に変化する大量のデータを逐一記録するときなどに使われる。
> HDF5のデータはデータセットとグループという単位からなる。

Convolutional Neural Network(CNN: 畳み込みニューラルネットワーク)
