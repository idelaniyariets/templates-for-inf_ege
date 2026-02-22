from math import dist


s = open("files/27_A_23209.txt")
s.readline()
data = []
for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1]
    if cluster:
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
px = int((min(centroids[0]))*10000)
py = int((min(centroids[1])*10000))


s = open("files/27_B_23209.txt")
s.readline()
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

centroids = [centroid(cluster) for cluster in clusters]

def get_len(centroid):
    for cluster in clusters:
        if centroid in cluster:
            return len(cluster)

lst = [[get_len(centroid), centroid] for centroid in centroids]
qx = int((abs(max(lst)[1][0] - min(lst)[1][0]))*10000)
qy = int(abs(max(lst)[1][1] - min(lst)[1][1])*10000)

print(px,py)
print(qx,qy)