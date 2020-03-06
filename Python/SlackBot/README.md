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
├── settings.py
├── run.py
└── plugins
    ├── __init__.py
    └── my_slackbot.py
```

### code

```Python:settings.py
API_TOKEN = '<API Token>'
DEFAULT_REPLY = 'おみくじを引いてみては？'
PLUGINS = ['plugins']
```

```Python:settings.py
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    main()
```

```Python:plugins/my_slackbot.py
from slackbot.bot import respond_to
import random

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(['大吉', '吉', '中吉', '小吉', '末吉', '凶', '大凶']))
```

## Run

```sh
python run.py
```