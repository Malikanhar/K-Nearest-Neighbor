import numpy as np

def dist(x,y):   
    return np.sqrt(np.sum((x-y)**2))

def getElm(elm):
    return elm[1]

def klasifikasi(list_kelas, k):
    d = {}
    d[0] = d[1] = d[2] = d[3] = 0
    for i in range(k):
        d[list_kelas[i][0]] += 1
    return max(d, key=d.get)

def isKlasifikasi(a, b):
    return a == b

csv = np.genfromtxt ('DataTrain_Tugas3_AI.csv', delimiter=",")
data = np.asarray(csv[1:,:])

np.random.shuffle(data)

for k in range(1,30,1):
    total = 0
    for i in range(800):
        dataTrain = list(data)
        v = dataTrain[i]
        dataTrain.pop(i)
        fin = []
        result = []
        for train in dataTrain:
            result.append([train[6], dist(train[1:6], v[1:6])])
        result.sort(key = getElm)
        if(isKlasifikasi(klasifikasi(result, k), v[6])):
            total += 1
    print("K =", k, "Average Acc =", total/800, "%")