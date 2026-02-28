from ipaddress import *

net = ip_network("109.231.10.50/255.255.255.0", 0)
print(net[-1])
#109+231+10+254 = 586