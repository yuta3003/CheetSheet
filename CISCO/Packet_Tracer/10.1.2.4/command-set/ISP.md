```
enable
config t
hostname ISP

enable secret class

line con 0
password cisco
login
logging synchronous
exit

line vty 0 4
password cisco
login
logging synchronous
exit

interface s0/0/1
ip address 209.165.200.225 255.255.255.224
no shutdown
exit

ip route 192.168.0.0 255.255.252.0 209.165.200.226
```