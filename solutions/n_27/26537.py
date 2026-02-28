from math import dist

s = open('files/27A_26537.txt')
data = []
for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1.2]
    if cluster:
        for p in cluster:
            data.remove(p)
        next_cl = [get_cluster(p) for p in cluster]
        cluster += sum(next_cl, [])
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

centroids = [centroid(cluster) for cluster in clusters]
sx = abs(int(sum([x[0] for x in centroids]) * 10000))
sy = abs(int(sum([x[1] for x in centroids]) * 10000))


s = open("files/27B_26537.txt")
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

q1 = abs(int((max([x[0] for x in max(clusters, key=len)]) * 10000)))
q2 = abs(int(max([x[1] for x in min(clusters, key=len)]) * 10000))

print(sx, sy)
print(q1,q2)