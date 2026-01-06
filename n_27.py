from math import dist

a = open("27_A_23766.txt") #открываем файл

data = []
for line in a:
    #чтение файла в список data
    data.append([float(x) for x in line.split()])

def get_cluster(p0):
    #проведение кластеризации. алгоритм DBSCAN
    cluster = [p for p in data if dist(p0, p)<1]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
while data:
    #завершаем кластреризацию, формируя список кластеров
    cluster = get_cluster(data[0])
    clusters.append(cluster)

def centroid(cluster):
    #получаем центроид кластера
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]
centroids = [centroid(cluster) for cluster in clusters]#формируем список центроидов
#обработка по условию. она не бывает шаблонной, придется подумать
px = int(min(x for x,y in centroids)*10000)
py = int(min(y for x, y in centroids)*10000)
print(px, py)

#файл B. логика не особо отличается
a = open("27_B_23766.txt")

data = []
for line in a:
    data.append([float(x) for x in line.split()])

def get_cluster(p0):
    cluster = [p for p in data if dist(p0, p)<1]
    if len(cluster) != 0:
        for p in cluster:
            data.remove(p)
        next_clusters = [get_cluster(p) for p in cluster]
        cluster += sum(next_clusters, [])
    return cluster

clusters = []
while data:
    cluster = get_cluster(data[0])
    clusters.append(cluster)

for cluster in clusters[::]:
    if len(cluster) == 1:
        clusters.remove(cluster)

def centroid(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

def find_cluster(p0, clusters):
    for cluster in clusters:
        if p0 in cluster:
            return len(cluster)

centroids = [centroid(cluster) for cluster in clusters]
#обработка по условию. она не бывает шаблонной, придется подумать
m = []
for dot in centroids:
    m.append([dot, find_cluster(dot, clusters)])
print(int(dist(m[0][0], m[1][0]))*10000)
m = []
for centroid in centroids:
    for cluster in clusters:
        if centroid in cluster:
            m.append(max([dist(centroid, dot) for dot in cluster]))
print(int(max(m)*10000))
#не рекомендую писать 2 блока кода для 2х файлов. здесь указано, как образец
#в условиях экзамена можно обойтись заменой файла и обработки условия