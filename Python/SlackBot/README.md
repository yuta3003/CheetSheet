# SlackBot

- [Create Bot Account](#create-bot-account)

## Create Bot Account
Slackへログインし、以下のサイトからBotアカウントを作成
[https://my.slack.com/services/new/bot](https://my.slack.com/services/new/bot)

API Token を取得

## Coding
### 構成
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

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))
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