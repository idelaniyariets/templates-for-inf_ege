from ipaddress import *

net = [ip for ip in ip_network('73.148.145.65/255.224.0.0', 0).hosts()]
print(net[-1])
