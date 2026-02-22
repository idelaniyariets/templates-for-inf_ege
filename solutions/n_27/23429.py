from math import dist


s = open("files/27A_23429.txt")
data = []
for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 2.6]
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
px = int((sum([centroids[i][0] for i in range(len(centroids))]))*10000)
py = int((sum([centroids[i][1] for i in range(len(centroids))]))*10000)


s = open("files/27B_23429.txt")
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
q1 = int((min([dist((0,0), centroid) for centroid in centroids]))*10000)
q2 = int((max([dist((0,0), centroid) for centroid in centroids]))*10000)

print(px,py)
print(q1,q2)