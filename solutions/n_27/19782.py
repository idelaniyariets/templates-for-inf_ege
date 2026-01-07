from math import dist

a = open("27A_19782.txt")
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

def radius(centroid):
    dists = []
    for cluster in clusters:
        if centroid in cluster:
            dists = [dist(centroid, dot) for dot in cluster]
    return max(dists)

centroids = [centroid(cluster) for cluster in clusters]
radii = [radius(centroid) for centroid in centroids]
print(int(min(radii)*10000), int(max(radii)*10000))


a = open("27B_19782.txt")
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<0.5]
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

def radius(centroid):
    dists = []
    for cluster in clusters:
        if centroid in cluster:
            dists = [dist(centroid, dot) for dot in cluster]
    return max(dists)

centroids = [centroid(cluster) for cluster in clusters]
radii = [radius(centroid) for centroid in centroids]
print(int(min(radii)*10000), int(max(radii)*10000))