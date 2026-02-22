'''
№ 18678 (Уровень: Сложный)'''
from math import dist
from turtle import *

a = open("files/27A_18678.txt")
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1.54]
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

for cluster in clusters[::]:
    if len(cluster)<30:
        clusters.remove(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = int((sum([x for x,y in centroids])/len(centroids))*100000)
py = int((sum([y for x,y in centroids])/len(centroids))*100000)
print(px, py)


a = open("files/27B_18678.txt")
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1.54]
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

tracer(0)
up()
i = -1
colors = ["red", "green", "blue", "black", "purple", "cyan", "orange"]
for cluster in clusters:
    i += 1
    for p in cluster:
        goto(p[0]*10, p[1]*10)
        dot(5, colors[i])
update()
exitonclick()

for cluster in clusters[::]:
    if len(cluster)<30:
        clusters.remove(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = int((sum([x for x,y in centroids])/len(centroids))*100000)
py = int((sum([y for x,y in centroids])/len(centroids))*100000)
print(px, py)