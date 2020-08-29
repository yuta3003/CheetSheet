# Router

- [COMMAND-SET](#COMMAND-SET)
- [解説](#解説)
    - [初期化方法](#初期化方法)
    - [特権EXECモードに切り替える](#特権EXECモードに切り替える)
    - [configurationモードに切り替える](#configurationモードに切り替える)
    - [hostname設定](#hostname設定)
    - [IPアドレス設定](#IPアドレス設定)
    - [不要なDNS-lookupを防止](#不要なDNS-lookupを防止)
    - [ローカルパスワード設定](#ローカルパスワード設定)
        - [特権EXECモード移行時PASSWORD要求を設定](#特権EXECモード移行時PASSWORD(class)要求を設定)
        - [接続時PASSWORD要求を設定](#接続時PASSWORD(cisco)要求を設定)
            - [コンソールポート](#コンソールポート)
            - [VTY](#VTY)
        - [パスワードを暗号化](#パスワードを暗号化)
    - [ログインバナーを設定](#ログインバナーを設定)
    - [設定を保存](#設定を保存)

## COMMAND-SET

```
enable
erase strtup-config
reload
config t
hostname xxx
enable secret xxx
no ip domain-lookup

banner motd #
Unauthorized access is strictly prohibited and prosecuted to the full extent of the law. #

line con 0
password xxx
login
logging synchronous
exit

line vty 0 4
password xxx
login
logging synchronous
exit

interface g0/0
ip address 192.168.0.1 255.255.255.0
no shutdown
description xxx
exit

interface g0/1
ip address 192.168.1.1 255.255.255.0
no shutdown
description xxx
exit

router rip
version 2
network 192.168.0.0
network 192.168.1.0
network 192.168.2.0
no auto-summary
```

## 解説
### 初期化方法
- startup-configの削除
- ルータの再起動

```
R1# erase startup-config
R1# reload
```

### 特権EXECモードに切り替える

```
Router> enable
Router#
```

### configurationモードに切り替える

```
Router# configure terminal
Router(config)#
```

### hostname設定

```
Router(config)# hostname R1
R1(config)#
```

### IPアドレス設定

```
R1# config t
R1(config)# interface xxx
R1(config-if)# ip address xxx.xxx.xxx.xxx xxx.xxx.xxx.xxx
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# 
```

### インターフェイスに説明を付加

```
R1(config)# interface xxx
R1(config-if)# description foo
R1(config-if)# exit
R1(config)# 
```

### 不要なDNS-lookupを防止

```
R1(config)# no ip domain-lookup
```

### ローカルパスワード設定する
#### 特権EXECモード移行時PASSWORD(class)要求を設定

```
R1(config)# enable secret class
```

#### 接続時PASSWORD(cisco)要求を設定
##### コンソールポート

```
R1(config)# line con 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
```
##### VTY

```
R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
```
#### パスワードを暗号化

```
R1(config)# service password-encryption
```
#### パスワード設定時min-length設定

```
R1(config)# security passwords min-length 10
```

### ログインバナーを設定

```
R1(config)# banner motd #
Unauthorized access is strictly prohibited and prosecuted to the full extent of the law. #
R1(config)# exit
R1#
```

### ルーティング設定
#### スタティックルート

```
R1(config)# ip route <address> <mask> {<next-hop> | <interface>}

取り除く場合は
R1(config)# no ip route <address> <mask>
```
#### デフォルトルート

```
R1(config)# ip route 0.0.0.0 0.0.0.0 <next-hop> | <interface>
```
#### ダイナミックルート
##### RIP
- ルータが持つネットワーク
    - 192.168.2.0
    - 192.168.3.0

```
# クラス単位で有効化される
# 今回はClass C
# RIP 有効化
Router(config)#router rip
Router(config-router)#version 2

# バージョン2 はクラス単位で有効化される
#   可変長サブネットに対応
#   サブネットを指定しなくてもデータのやりとりで取得する

# バージョン1 は固定長サブネットで使用可能


# ルータが持つネットワークを指定する
Router(config-router)#network 192.168.2.0
Router(config-router)#network 192.168.3.0
Router(config-router)#exit
Router(config)#

# 自動集約をOFFにするのは
no auto-summary
```
##### OSPF

```
Router(config)#interface g0/0
Router(config-if)#ip address 172.16.0.1 255.255.0.0
Router(config-if)#no shutdown
Router(config-if)#exit

Router(config)#interface s0/0/0
Router(config-if)#ip address 192.168.1.1 255.255.255.0
Router(config-if)#clock rate 64000
Router(config-if)#bandwidth 64
Router(config-if)#no shutdown
Router(config-if)#exit

Router(config)#interface s0/0/1
Router(config-if)#ip address 192.168.5.2 255.255.255.0
Router(config-if)#bandwidth 64
Router(config-if)#no shutdown
Router(config-if)#exit

Router(config-router)#router ospf 1
Router(config-router)#network 172.16.0.0 0.0.255.255 area 0
Router(config-router)#network 192.168.1.0 0.0.0.255 area 0
Router(config-router)#network 192.168.5.0 0.0.0.255 area 0
Router(config-router)#exit
```

### 設定を保存
copy コマンドを使用して、Non-Volatile Random Access Memory（NVRAM; 不揮発性 RAM）にあるスタートアップ ファイルに実行コンフィギュレーションを保存します。

```
R1# copy running-config startup-config
Destination filename [startup-config]? [Enter]
Building configuration...
[OK]
R1#
```
