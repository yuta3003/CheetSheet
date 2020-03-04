# Scapy

- [install](#install)
- [import](#import)
- [How To use](#How-To-use)
    - [Create Packet](#create-packet)
    - [Resolve Mac Address](#resolve-mac-address)

## install
```sh
pip install scapy
```

## import
```python
from scapy.all import *
```

## How To use

### Create Packet

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
# The protocol is defined as a class.
# Multiple layers of packets can be created by separating them with /.

Ether()/IP()/TCP()
packet = (Ether(src="11:11:11:11:11:11",dst="11:11:11:11:11:11")
    /IP(src="192.168.1.1",dst="192.168.1.2")
    /TCP(sport=1234, dport=4321, flags="S"))
```

### Resolve MAC Address

ipアドレスからMACアドレスを取得する
```Python
responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=2, retry=10)
for s, r in responses:
    print(r[Ether].src)
```