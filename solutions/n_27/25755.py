from math import dist

a = open("files/27A_25755.txt")
data = []

for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1]
    if cluster:
        for p in cluster:
            data.remove(p)
        nextcl = [get_cluster(p) for p in cluster]
        cluster += sum(nextcl, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def fmin(cl1, cl2):
    dots = []
    mdist = 100000000
    for star in cl1:
        for star1 in cl2:
            dists = dist(star, star1)
            if dists < mdist:
                dots = [star, star1]
                mdist = dists
    return dots

px = py = 0

res = []
for i in range(len(clusters)):
    for j in range(i, len(clusters)):
        res.append(fmin(clusters[i], clusters[j]))
print(res)
print((sum([dot[0] for pair in res for dot in pair])/12)*10000)
for dot in res:
    px += dot[0][0]+dot[1][0]
    py += dot[0][1]+dot[1][1]
print(int((px/12)*10000), int((py/12)*10000))

s = open("files/27B_25755.txt")
data = []

for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

for cluster in clusters[::]:
    if len(cluster) == 1:
        clusters.remove(cluster)

res = []
for i in range(len(clusters)):
    for j in range(i+1, len(clusters)):
        res.append(fmin(clusters[i], clusters[j]))

q = (fmin(sorted(clusters, key=len)[0], sorted(clusters, key=len)[-1]))
q1 = int(dist(q[0], q[1])*10000)
q2 = int((max(dist(p, (0,0)) for dots in res for p in dots))*10000)
print(q1, q2)
