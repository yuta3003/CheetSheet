enable
config t
hostname ISP
enable secret class
no ip domain-lookup

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

interface s0/0/0
ip address 209.165.201.17 255.255.255.252
no shutdown
clock rate 1280000
exit

interface lo0
ip address 192.31.7.1 255.255.255.255
no shutdown
exit

interface g0/0
ip address 209.165.202.1 255.255.255.0
no shutdown
exit

username webuser privilege 15 secret webpass

ip route 209.165.200.224 255.255.255.224 209.165.201.18