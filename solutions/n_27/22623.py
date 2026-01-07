from math import dist

a = open("27A_22623.txt")
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

def density(cluster):
    area = 16
    return len(cluster)/area

def get_len(dot, clusters):
    for p in clusters:
        if dot in p:
            return len(p)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
densities = [density(cluster) for cluster in clusters]
sspp = [[get_len(centroid, clusters)/16, centroid] for centroid in centroids]
ps = int((sum(densities)/len(densities))*1000)
sp = int(dist(max(sspp)[1], min(sspp)[1])*1000)
print(ps, sp)


a = open("27B_22623.txt")
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

def density(cluster):
    area = 16
    return len(cluster)/area

def get_len(dot, clusters):
    for p in clusters:
        if dot in p:
            return len(p)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
densities = [density(cluster) for cluster in clusters]
sspp = [[get_len(centroid, clusters)/16, centroid] for centroid in centroids]
ps = int((sum(densities)/len(densities))*1000)
sp = int(dist(max(sspp)[1], min(sspp)[1])*1000)
print(ps, sp)