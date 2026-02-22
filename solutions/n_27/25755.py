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

res = [fmin(clusters[0], clusters[1]), fmin(clusters[1], clusters[2]), fmin(clusters[0], clusters[2])]
for dot in res:
    px += dot[0][0]+dot[1][0]
    py += dot[0][1]+dot[1][1]
print(int((px/6)*10000), int((py/6)*10000))