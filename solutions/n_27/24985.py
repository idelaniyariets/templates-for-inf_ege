from math import dist

a = open("files/27A_24985.txt")
data = []

for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next = [get_cluster(p) for p in cluster]
        cluster += sum(next, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

for cluster in clusters[::]:
    if len(cluster) == 1:
        clusters.remove(cluster)

def acentroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p0) for p0 in cluster)
        m.append([sm, p])
    return max(m)[1]

anti_centroids = [acentroid(cluster) for cluster in clusters]
px = max(anti_centroids)[0]
py = max(anti_centroids)[1]

a = open("files/27B_24985.txt")
data = []

for line in a:
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

def get_len(ac):
    for cluster in clusters:
        if ac in cluster:
            return len(cluster)

def get_max(dot):
    dists = []
    for cluster in clusters:
        if dot in cluster:
            dists = [dist(dot, p) for p in cluster]
            break
    return max(dists)

anti_centroids = [acentroid(cluster) for cluster in clusters]
ls = [[get_len(ac), ac] for ac in anti_centroids]
ds = [get_max(ac) for ac in anti_centroids]
qx = dist(max(ls)[1], min(ls)[1])
qy = max(ds)

print(int(px*10000), int(py*10000))
print(int(qx*10000), int(qy*10000))