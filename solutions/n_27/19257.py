from math import dist
s = open("27_A_19257.txt")
s.readline()
data = []
for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1.8]
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
        sm = sum(dist(p, p0) for p0 in cluster)
        m.append((sm, p))
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = int((sum([centroid[0] for centroid in centroids])/len(centroids))*10000)
py = int((sum([centroid[1] for centroid in centroids])/len(centroids))*10000)

s = open("27_B_19257.txt")
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

centroids = [centroid(cluster) for cluster in clusters]
qx = int((sum([centroid[0] for centroid in centroids])/len(centroids))*10000)
qy = int((sum([centroid[1] for centroid in centroids])/len(centroids))*10000)

print(px, py)
print(qx, qy)