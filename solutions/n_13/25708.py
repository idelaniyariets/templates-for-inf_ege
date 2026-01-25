from ipaddress import *

net = ip_network("212.154.18.25/255.255.255.0", 0)
k = 0

for ip in net.hosts():
    k += 1

print(k)