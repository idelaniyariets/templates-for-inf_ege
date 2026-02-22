'''№ 23571 Пересдача 03.07.25 (Уровень: Базовый)'''
from math import dist

a = open("files/27_A_23571.txt")
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
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = int(sum([x for x,y in centroids])*10000)
py = int(sum([y for x,y in centroids])*10000)
print(px, py)


a = open("files/27_B_23571.txt")
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

'''1) пребор расстояний от каждой точки до каждой точки
2) думаю... спасибо господину А. Кабанову за решение'''
def minr(cl1, cl2):
    m = []
    for p1 in cl1:
        for p2 in cl2:
            m.append(dist(p1, p2))
    return min(m)

def maxr(cl1, cl2):
    m = []
    for p1 in cl1:
        for p2 in cl2:
            m.append(dist(p1, p2))
    return max(m)
q1 = int(min([minr(clusters[0], clusters[1]), minr(clusters[0], clusters[2]), minr(clusters[1], clusters[2])])*10000)
q2 = int(max([maxr(clusters[0], clusters[1]), maxr(clusters[0], clusters[2]), maxr(clusters[1], clusters[2])])*10000)
print(q1, q2)