import numpy as np
from math import sqrt
import pandas as pd


def euclidian_distance(X_origin , X_predict):
    sum = 0
    for i in range(len(X_origin)):
        sum+= ((X_origin[i] - X_predict[i])**2)
    return sqrt(sum)

df = pd.read_csv('Train.csv')
df.drop(['ID'],1, inplace=True)

X = np.array(df.drop(['y'],1))
y = np.array(df['y'])

benar = 0
total = 0

for i in range(11):
    result_distance = []
    for j in range(len(df) - 1):
        rset = euclidian_distance(X[i], X[j])
        result_distance.append((rset , y[j]))

    result_distance = sorted(result_distance)

    count0 = 0
    count1 = 1

    for k in range(5):
        if result_distance[k][1] == 0:
            count0 +=1
        else:
            count1+=1
    if(count0>count1):
        kelas_prediksi= 0
    else:
        kelas_prediksi = 1

    if kelas_prediksi==y[i]:
        benar+=1

    total+=1
    print(benar,total)
    del(result_distance)

print(benar / total)
