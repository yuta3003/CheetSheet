# SlackBot

- [Create Bot Account](#create-bot-account)
- [install package](#install-package)
- [Coding](#coding)
    - [Constitution](#constitution)
    - [code](#code)
        - [settings.py](#settings)
        - [run.py](#run)
        - [my_slackbot.py](#my_slackbot)
- [Run on Local](#run-on-local)
- [Deploy on Heroku](#deploy-on-heroku)
    - [code](#code)
        - [Procfile](#procfile)
        - [requirements.txt](#requirements.txt)
        - [.gitignore](#.gitignore)
    - [Deploy](#deploy)
    - [Run on Heroku](#run-on-heroku)
- [References](#references)

## Create Bot Account
Slackへログインし、以下のサイトからBotアカウントを作成
[https://my.slack.com/services/new/bot](https://my.slack.com/services/new/bot)

API Token を取得

## install package
```
pip install slackbot
```
## Coding
### Constitution
```
heroku-slack-bot
├── .gitignore
├── settings.py
├── run.py
├── Procfile
├── requirements.txt
└── plugins
    ├── __init__.py
    └── my_slackbot.py
```

### code
#### settings
```Python:settings.py
API_TOKEN = '<API Token>'
DEFAULT_REPLY = 'おみくじを引いてみては？'
PLUGINS = ['plugins']
```

#### run
```Python:run.py
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
```

#### my_slackbot
```Python:plugins/my_slackbot.py
from slackbot.bot import respond_to
import random

# 特定の単語に反応
@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))
```
##### 特定の単語に反応
```Python
@respond_to('Hello')
def reply_hello(message):
    message.reply('Hello')
```
##### メッセージを変数として受け取る
```Python
@respond_to('(.*)')
def reply_hello(message, arg):
    message.reply(arg)
```

##### 正規表現を使用
```Python
@respond_to('[a-zA-Z]\sうさぎ')
def reply_hello(message):
    message.reply('どうしたの？')
```

##### 複数のコメントを受け取る
```Python
@respond_to('(.*) (.*)')
def reply_hello(message, arg1, arg2):
    message.reply(arg1 + ': ' + arg2)
```

##### 記号付き複数メッセージ
コマンドをオプション付きで読み込むときに使用
```Python
@respond_to('(.*)\s(\-[a-zA-Z])')
def reply_hello(message, command, arg):
    message.reply(command + ' ' + arg + 'ですね')
```

##### 発言に対してスタンプをつける
```Python
@respond_to('(スライムベス|スライム)')
def reply_hello(message, name):
    if name == 'スライムベス':
        message.react('slimebess')
    elif name == 'スライム':
        message.react('slime')
```

##### メッセージを整形する
[使用可能パラメータ](https://api.slack.com/docs/messages/builder?msg=%7B%22attachments%22%3A%5B%7B%22fallback%22%3A%22Required%20plain-text%20summary%20of%20the%20attachment.%22%2C%22color%22%3A%22%2336a64f%22%2C%22pretext%22%3A%22Optional%20text%20that%20appears%20above%20the%20attachment%20block%22%2C%22author_name%22%3A%22Bobby%20Tables%22%2C%22author_link%22%3A%22http%3A%2F%2Fflickr.com%2Fbobby%2F%22%2C%22author_icon%22%3A%22http%3A%2F%2Fflickr.com%2Ficons%2Fbobby.jpg%22%2C%22title%22%3A%22Slack%20API%20Documentation%22%2C%22title_link%22%3A%22https%3A%2F%2Fapi.slack.com%2F%22%2C%22text%22%3A%22Optional%20text%20that%20appears%20within%20the%20attachment%22%2C%22fields%22%3A%5B%7B%22title%22%3A%22Priority%22%2C%22value%22%3A%22High%22%2C%22short%22%3Afalse%7D%5D%2C%22image_url%22%3A%22http%3A%2F%2Fmy-website.com%2Fpath%2Fto%2Fimage.jpg%22%2C%22thumb_url%22%3A%22http%3A%2F%2Fexample.com%2Fpath%2Fto%2Fthumb.png%22%2C%22footer%22%3A%22Slack%20API%22%2C%22footer_icon%22%3A%22https%3A%2F%2Fplatform.slack-edge.com%2Fimg%2Fdefault_application_icon.png%22%2C%22ts%22%3A123456789%7D%5D%7D)
```Python
@respond_to('usagi')
def reply_hello(message):
    attachments = [
        {
            "color": "#3104B4",
            "fields": [
                {
                    "title": "場所",
                    "value": "東京駅"
                },
                {
                    "title": "時間",
                    "value": "19:00"
                }
            ],
            "footer": "usagi-san",
            "footer_icon": "https://pics.prcm.jp/db36726f85742/67433428/jpeg/67433428.jpeg"
        }
    ]
    message.send_webapi('集合場所', json.dumps(attachments))
```

## Run on Local

ローカルで動作確認

```sh
python run.py
```

## Deploy on Heroku
### code
#### Procfile
Heroku設定用ファイルProcfileを編集
```Procfile
worker: python run.py
```

#### requirements.txt
```
slackbot
```

#### .gitignore
```
__pycache__
Dockerfile
```

### Deploy
```
git init
git add .
git commit -m "first commit"

heroku login
heroku create <app_name>
git push heroku master
```

### Run on Heroku
[Heroku ダッシュボード](https://dashboard.heroku.com/apps)からworkerをONにする

以下のコマンドでログの確認可能
```
heroku logs --tail
```

## References
- [[Slack]Botkitをherokuの無料プランで動かす方法](https://qiita.com/biga816/items/148a1156cd8b1a964b91)
- [PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)
- [Github - lins05/slackbot](https://github.com/lins05/slackbot/tree/develop/slackbot)
- [Slack API](https://api.slack.com/web)
- [Pythonの正規表現操作](https://docs.python.jp/3/library/re.html)
- [Qiita - PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)