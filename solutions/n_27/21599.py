from math import dist
from turtle import *
import time

a = open("27_A_21599.txt")

data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<4.9]
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
colors = ["red", "green", "blue", "purple", "orange", "black", "cyan"]
i = 0
for cluster in clusters:
    i += 1
    for dote in cluster:
        goto(dote[0]*5, dote[1]*5)
        dot(5, colors[i])
update()
#time.sleep(2)
#из соображений визуализации:
dt = clusters.pop(1)
print(clusters[0])
i = 0
for cluster in clusters:
    i += 1
    for dote in cluster:
        goto(dote[0]*5, dote[1]*5)
        dot(5, colors[i])
update()
exitonclick()

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum([dist(p, p0) for p0 in cluster])
        m.append([sm, p])
    return min(m)[1]

centroids = [centroid(cluster) for cluster in clusters]
px = abs(int(sum([x for x, y in centroids])/len(centroids)*10000))
py = abs(int(sum([y for x,y in centroids])/len(centroids)*10000))
print(px, py)


a = open("27_B_21599.txt")
data = []
for line in a:
    data.append([float(x) for x in line.split()])
print(len(data))

def get_cluster(p0):
    cluster = [p for p in data if dist(p, p0)<1.5]
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
        m.append([sm, p])
    return min(m)[1]
centroids = [centroid(cluster) for cluster in clusters]
px = abs(int(sum([x for x, y in centroids])/len(centroids)*10000))
py = abs(int(sum([y for x, y in centroids])/len(centroids)*10000))
print(px, py)

