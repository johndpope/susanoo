# サンプルについて
## 注意点
* サンプルコード（python 2 系）と python 3 系 の違いで気を付けること
  * print は () で囲む
  * map は 添え字でアクセスできないので list() で囲む
    * for in を使えばスマート
```python
# 以下は同じ
v = list(map(int, line.split()))
v = [i for i in line.split()]
```
