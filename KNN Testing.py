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

csv = np.genfromtxt ('DataTrain_Tugas3_AI.csv', delimiter=",")
dataTrain = np.asarray(csv[1:,:])

csv = np.genfromtxt ('DataTest_Tugas3_AI.csv', delimiter=",")
dataTest = np.asarray(csv[1:,:])

fin = []
k = 8 # nilai k didapat berdasarkan hasil Train K
for test in dataTest:
    result = []
    for train in dataTrain:
        result.append([train[6], dist(train[1:6], test[1:6])])
    result.sort(key = getElm)
    fin.append(klasifikasi(result, k))
np.savetxt("TebakanTugas3.csv", fin, delimiter=", ", fmt='%s')
print("Program berhasil dijalankan, silahkan buka file TebakanTugas3.csv untuk melihat hasilnya")