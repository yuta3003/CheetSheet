# Scapy

## パッケージインストール
```sh
pip install scapy
```

## インポート
```python
from scapy.all import *
```

## パケット生成

```Python
"""
- Ethernet
    - Src MAC Addr: 00:00:00:00:00:00
    - Dst MAC Addr: 11:11:11:11:11:11
- IP
    - Src IP Addr: 192.168.1.1
    - Dst IP Addr: 192.168.1.2
- TCP
    - Src port: 1234
    - Dst port: 4321
    - Flag: SYN
"""
# 上記のようなパケットを作成する場合

Ether()/IP()/TCP()
packet = (Ether(src="11:11:11:11:11:11",dst="11:11:11:11:11:11")
    /IP(src="192.168.1.1",dst="192.168.1.2")
    /TCP(sport=1234, dport=4321, flags="S"))
```