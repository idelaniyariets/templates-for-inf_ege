from math import dist

a = open("27_A_23384.txt")
a.readline()
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1]
    for p in cluster:
        data.remove(p)
    next_clusters = [get_cluster(p) for p in cluster]
    cluster += sum(next_clusters, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p0) for p0 in cluster)
        m.append([sm, p])
    return min(m)[1]
centroids = [centroid(cluster) for cluster in clusters]
px = int((sum(x for x,y in centroids)*10000))
py = int(sum([y for x,y in centroids])*10000)
print(px, py)


a = open("27_B_23384.txt")
a.readline()
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1]
    for p in cluster:
        data.remove(p)
    next_clusters = [get_cluster(p) for p in cluster]
    cluster += sum(next_clusters, [])
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
        sm = sum(dist(p, p0) for p0 in cluster)
        m.append([sm, p])
    return min(m)[1]
centroids = [centroid(cluster) for cluster in clusters]
m = []
for centroid in centroids:
    m.append(dist(centroid, [0,0]))
q1 = int(min(m)*10000)
q2 = int(max(m)*10000)
print(q1, q2)