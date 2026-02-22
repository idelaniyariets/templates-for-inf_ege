from math import dist

a = open("files/27A_22625.txt")
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

def anti_centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return max(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
anti_centroids = [anti_centroid(cluster) for cluster in clusters]
px = int(((centroids[0][0]+centroids[1][0])/len(centroids))*10000)
sy = int(((anti_centroids[0][1]+anti_centroids[1][1])/len(anti_centroids))*10000)
print(px, sy)


a = open("files/27B_22625.txt")
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

def anti_centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return max(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
anti_centroids = [anti_centroid(cluster) for cluster in clusters]
px = int(((centroids[0][0]+centroids[1][0]+centroids[2][0])/len(centroids))*10000)
sy = int(((anti_centroids[0][1]+anti_centroids[1][1]+anti_centroids[2][1])/len(anti_centroids))*10000)
print(px, sy)