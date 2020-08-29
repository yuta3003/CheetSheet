enable
config t
hostname GATEWAY
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

interface g0/1
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface s0/0/1
ip address 209.165.201.18 255.255.255.252
no shutdown
exit

ip route 0.0.0.0 0.0.0.0 209.165.201.17

ip nat inside source static 192.168.1.20 209.165.200.225

interface g0/1
ip nat inside
exit

interface s0/0/1
ip nat outside
exit

access-list 1 permit 192.168.1.0 0.0.0.255

ip nat pool public_access 209.165.200.242 209.165.200.254 netmask 255.255.255.224
ip nat inside source list 1 pool public_access

no ip nat inside source static 192.168.1.20 209.165.200.225
