'''№ 24898 (Уровень: Средний)'''
from math import dist

a = open("27_A_24898.txt")
a.readline()
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster += sum(next_cluster, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

def get_len(dot, clusters):
    for cluster in clusters:
        if dot in cluster:
            return [len(cluster), dot[0]+dot[1]]
centroids = [centroid(cluster) for cluster in clusters]
lens = [get_len(p, clusters) for p in centroids]
px = int(min(lens)[1]*10000)
py = int(max(lens)[1]*10000)
print(px, py)


a = open("27_B_24898.txt")
a.readline()
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_cluster = [get_cluster(p) for p in cluster]
        cluster += sum(next_cluster, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

for cluster in clusters[::]:
    if len(cluster) == 1:
        clusters.remove(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

def get_len(dot, clusters):
    for cluster in clusters:
        if dot in cluster:
            return [len(cluster), dot[0]+dot[1]]
centroids = [centroid(cluster) for cluster in clusters]
dists = [[dist(centroid, [0,0]), centroid[0], centroid[1]] for centroid in centroids]
qx = int(max(dists)[1]*10000)
qy = int(min(dists)[2]*10000)
print(qx, qy)