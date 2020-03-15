# Find System Infomation

## システム情報を読み取る
以下は様々なモジュールを使用して`/etc/hosts`の情報をPythonから取得する。

### osモジュール
```Python
import os
os.uname()
```

### platfomモジュール
```Python
import platform
platform.uname()
```

## ディスク容量を読み取る
Linuxコマンドの`df`や`du`コマンドで取得する情報をPythonから取得する。

### shutilモジュールの場合
```Python
import shutil
shutil.disk_usage('/').total / 1024 ** 3  #  GBで取得
```

### osモジュールの場合
```Python
import os
_stat = os.statvfs('/')

# ディスク容量 = フラグメントサイズ x ブロック数
_stat.f_frsize() * _stat.f_blocks / 1024 ** 3
```

## プロセス情報を読み取る
Linuxコマンドの`ps`コマンドで取得できる情報をPythonから取得する。  
`pip install psutil`を実行してモジュールをインポートしておく必要がある。
```Python
import psutil
process_cnt = 0
for p in psutil.process_iter():
    print(p)
    process_cnt += 1

process_cnt
```