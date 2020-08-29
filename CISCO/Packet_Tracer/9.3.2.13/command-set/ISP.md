```
enable
config t

no ip domain-lookup
hostname ISP

interface Lo0
ip address 209.165.200.225 255.255.255.224
no shutdown
exit

interface Lo1
ip address 209.165.201.1 255.255.255.224
no shutdown
exit

interface S0/0/0
ip address 10.1.1.2 255.255.255.252
no shutdown
exit

interface S0/0/1
ip address 10.2.2.2 255.255.255.252
no shutdown
clock rate 128000
exit

enable secret class

line con 0
password cisco
login
logging synchronous
exit

line vty 0 4
password cisco
login local
logging synchronous
transport input telnet
exit

router rip
version 2

network 10.1.1.0
network 10.2.2.0
network 209.165.200.224
network 209.165.201.0

no auto-summary
```