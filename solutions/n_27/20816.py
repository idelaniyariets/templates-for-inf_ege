from math import dist

s = open('27_A_20816.txt')
s.readline()
data = []

for line in s:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0) < 1.5]
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

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = abs(int(((centroids[0][0] + centroids[1][0])/2) * 10000))
py = abs(int(((centroids[0][1] + centroids[1][1])/2) * 10000))

s = open("27_B_20816.txt")
s.readline()
data = []

for line in s:
    data.append([float(x) for x in line.split()])
print(len((data)))

clusters = []
while data:
    cluster = get_cluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

centroids = [centroid(cluster) for cluster in clusters]
px1 = abs(int(((centroids[0][0] + centroids[1][0] + centroids[2][0])/3) * 10000))
py1 = abs(int(((centroids[0][1] + centroids[1][1] + centroids[2][1])/3) * 10000))

print(px, py)
print(px1, py1)