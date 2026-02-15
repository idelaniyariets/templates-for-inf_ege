from ipaddress import *

net = ip_network("158.214.121.40/255.255.255.224", False)

for ip in net.hosts():
    pass
print(ip)