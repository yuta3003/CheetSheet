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