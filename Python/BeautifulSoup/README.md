# BeautifulSoup

- [install](#install)
- [import](#import)
- [How To use](#how-to-use)
- [References](#references)

## install
```sh
pip install beautifulsoup4
```

## import
```Python
import bs4
```

## How To use

### with requests
```sh
pip install requests
```

```Python
import requests
from bs4 import BeautifulSoup
res = requests.get('スクレイピングしたいURL')
soup = BeautifulSoup(res.text, 'html')

soup.select_one('タグとかセレクターとか指定する').text  # ここをいろいろ変えるよ

BeautifulSoup.find()    # タグを検索して最初にhitしたタグを返す
BeautifulSoup.find_all()    # タグを検索してhitしたタグのリストを返す
BeautifulSoup.find_previous()   # 一つ前のタグを返す
BeautifulSoup.find_next()   # 一つ後ろのタグを返す
BeautifulSoup.find_parent() # 親タグを返す
BeautifulSoup.select()      # css selectorでタグのリストを返す
BeautifulSoup.select_one()  # css selectorで検索して最初にhitしたタグを返す
```

上記命令軍は[ここ](https://github.com/pynyumon/pynyumon/blob/master/2_scraping.md)から引用しています

## References
- [https://github.com/pynyumon/pynyumon/blob/master/2_scraping.md](https://github.com/pynyumon/pynyumon/blob/master/2_scraping.md)