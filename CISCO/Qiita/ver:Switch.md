# Switch
- [初期化方法](#初期化方法)
- [特権EXECモードに切り替える](#特権EXECモードに切り替える)
- [configurationモードに切り替える](#configurationモードに切り替える)
- [本体情報を表示](#本体情報を表示)
- [hostname設定](#hostname設定)
- [IPアドレス設定](#IPアドレス設定)
- [デフォルトゲートウェイ設定](#デフォルトゲートウェイ設定)
- [不要なDNS-lookupを防止](#不要なDNS-lookupを防止)
- [ローカルパスワード設定](#ローカルパスワード設定)
    - [特権EXECモード移行時PASSWORD要求を設定](#特権EXECモード移行時PASSWORD(class)要求を設定)
    - [接続時PASSWORD要求を設定](#接続時PASSWORD(cisco)要求を設定)
        - [コンソールポート](#コンソールポート)
        - [VTY](#VTY)
    - [パスワードを暗号化](#パスワードを暗号化)
- [VLAN設定](#vlan設定)
    - [VLAN99を作成](#VLAN99を作成)
    - [名前を設定](#名前を設定)
- [SSH設定](#SSH設定)
    - [ドメイン作成](#ドメイン作成)
    - [ユーザー作成](#ユーザー作成)
    - [VTYをSSH接続専用に設定](#VTYをSSH接続専用に設定)
    - [RSA暗号キーの作成](#RSA暗号キーの作成)
    - [デフォルトSSH設定の変更](#デフォルトSSH設定の変更)
    - [SSHに接続する](#SSHに接続する)
- [ログインバナーを設定](#ログインバナーを設定)
- [ポートセキュリティ設定](#ポートセキュリティ設定)
    - [ポートセキュリティを有効化](#ポートセキュリティを有効化)
    - [ポートセキュリティ確認コマンド](#ポートセキュリティ確認コマンド)
        - [正常時](#正常時)
        - [異常時](#異常時)
- [設定を確認](#設定を確認)
    - [現在のコンフィグレーション](#現在のコンフィグレーション)
    - [保存されたコンフィグレーション](#保存されたコンフィグレーション)
- [設定を保存](#設定を保存)

## 初期化方法
- startup-configの削除
- vlan.datの削除
- Switchの再起動
```
erase startup-config
delete vlan.dat
reload
```

## 特権EXECモードに切り替える
```
Switch> enable
Switch#
```

## configurationモードに切り替える
```
Switch# configure terminal
Switch(config)#
```

## 本体情報を表示
```
Switch# config t
Switch(config)# show version
```
- IOSソフトウェアの情報
- IOSソフトウェアのバージョン情報
- ブートROMのバージョン
- スイッチを起動してからの経過時間
- 起動した原因
- 起動に使用したIOSソフトウェアの場所とファイル名
- Cataliystスイッチ本体のモデル名(機種)
- Memoryサイズ
- 作成されたVLANインターフェイスの数
- NVRAMのサイズ
- コンフィグレーションレジスタの値

## hostname設定
```
Switch(config)# hostname S1
S1(config)#
```

## IPアドレス設定
```
S1# config t
S1(config)# interface XXX
S1(config-if)# ip address XXX.XXX.XXX.XXX XXX.XXX.XXX.XXX
S1(config-if)# no shutdown
S1(config-if)# exit
S1(config)# 
```
## デフォルトゲートウェイ設定
```
S1# config t
S1(config)# ip default-gateway XXX.XXX.XXX.XXX
```

## 不要なDNS-lookupを防止
```
S1(config)# no ip domain-lookup
```

## ローカルパスワード設定
### 特権EXECモード移行時PASSWORD(class)要求を設定
```
S1(config)# enable secret class
```
### 接続時PASSWORD(cisco)要求を設定
#### コンソールポート
```
S1(config)# line con 0
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
```
#### VTY
```
S1(config)# line vty 0 4
S1(config-line)# password cisco
S1(config-line)# login
S1(config-line)# exit
```
### パスワードを暗号化
```
S1(config)# service password-encryption
```

## VLAN設定
### VLAN99を作成
```
S1(config)# vlan 99
S1(config-vlan)# exit
S1(config)#
```
### 名前を設定
```
S1(config)# vlan 99
S1(config-vlan)# name hoge 
S1(config-vlan)# exit
S1(config)#
```
### VLANにポートを設定する
```
S1# show ip interface brief
    Status is up
    Protocol is Down
```
VLANにポートを設定しないとプロトコルがダウン状態になる
```
S1(config)# interface f0/5
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 99
S1(config-if)# exit
S1(config)#
```

## SSH設定
### ドメイン作成
```
S1(config)# ip domain-name hoge.com
```
### ユーザー作成
```
S1(config)# username admin privilege 15 secret sshadmin
```
### VTYをSSH接続専用に設定
SSH接続だけを許可するようにVTY回線のtransport inputを設定し、認証にローカルデータベースを使用する。
```
S1(config)# line vty 0 15
S1(config-line)# transport input ssh
S1(config-line)# login local
S1(config-line)# exit
```
### RSA暗号キーの作成
```
S1(config)# crypto key generate rsa
How many bits in the modulus [512]: 1024
```
### デフォルトSSH設定の変更
- SSHのタイムアウト設定を75秒
- SSHで許される認証試行回数
```
S1# config t
S1(config)# ip ssh time-out 75
S1(config)# ip ssh authentication-retries 2
```
### SSHに接続する
```
C:\> ssh -l admin XXX.XXX.XXX.XXX
Password:
```

## ログインバナーを設定
```
S1(config)# banner motd #
Unauthorized access is strictly prohibited and prosecuted to the full extent of the law. #
S1(config)# exit
S1#
```
## ポートセキュリティ設定
### ポートセキュリティを有効化
```
S1(config)# interface f0/5
S1(config-if)# shutdown
S1(config-if)# switchport port-security
S1(config-if)# switchport port-security mac-address XXXX.XXXX.XXXX
S1(config-if)# no shutdown
S1(config-if)# end
```
### ポートセキュリティ確認コマンド
#### 正常時
```
S1#show port-security
Secure Port MaxSecureAddr CurrentAddr SecurityViolation Security Action
               (Count)       (Count)        (Count)
--------------------------------------------------------------------
        Fa0/5        1          1                 0         Shutdown
----------------------------------------------------------------------
```
#### 異常時
ルータのmacアドレスをaaaa.bbbb.ccccに変更した場合に以下のような状態になった
```
S1#show port-security
Secure Port MaxSecureAddr CurrentAddr SecurityViolation Security Action
               (Count)       (Count)        (Count)
--------------------------------------------------------------------
        Fa0/5        1          1                 1         Shutdown
----------------------------------------------------------------------
```

## 設定を確認
### 現在のコンフィグレーション
```
S1# config t
S1(config)# show running-config
```
### 保存されたコンフィグレーション
```
S1# config t
S1(config)# show startup-config
```

## 設定を保存
copy コマンドを使用して、Non-Volatile Random Access Memory（NVRAM; 不揮発性 RAM）にあるスタートアップ ファイルに実行コンフィギュレーションを保存します。
```
S1# copy running-config startup-config
Destination filename [startup-config]? [Enter]
Building configuration...
[OK]
S1#
```
