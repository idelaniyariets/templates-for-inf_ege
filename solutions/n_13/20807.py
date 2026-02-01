from ipaddress import *

net = ip_network("172.16.192.0/255.255.192.0")
c = 0

for ip in net:
    bip = bin(int(ip)).zfill(32)[2:]
    if bip.count('1') % 5 != 0:
        c += 1

print(c)