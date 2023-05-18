# Algoritmo de cuadrados medios - Prueba de bondad y ajuste X²

from numpy import number
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot
import numpy as np
import random


n=1000
numeros=[]
semilla = 1390 #numero de + 3 digitos
tam1 = len(str(semilla))
numero1 = semilla
for i in range (0,n):
    numero2 = numero1**2
    snumero2 = str(numero2)
    tam2 = len(str(snumero2))
    primerc = (tam2-tam1)/2
    snumero2 = str(snumero2)
    snumero3 = snumero2[int(primerc):int(primerc+tam1)]
    numeros.append(int(snumero3))
    numero1 = int(snumero3)
print(numeros)

co=[0,0,0,0,0,0,0,0,0,0]

if (numeros[0] >= 0 and numeros[0] <= 999):
    co[0]=co[0] + 1
elif (numeros[0] >= 1000 and numeros[0] <= 1999):
    co[1]=co[1] + 1
elif (numeros[0] >= 2000 and numeros[0] <= 2999):
    co[2]=co[2] + 1
elif (numeros[0] >= 3000 and numeros[0] <= 3999):
    co[3]=co[3] + 1
elif (numeros[0] >= 4000 and numeros[0] <= 4999):
    co[4]=co[4] + 1
elif (numeros[0] >= 5000 and numeros[0] <= 5999):
    co[5]=co[5] + 1
elif (numeros[0] >= 6000 and numeros[0] <= 6999):
    co[6]=co[6] + 1
elif (numeros[0] >= 7000 and numeros[0] <= 7999):
    co[7]=co[7] + 1
elif (numeros[0] >= 8000 and numeros[0] <= 8999):
    co[8]=co[8] + 1
elif (numeros[0] >= 9000 and numeros[0] <= 9999):
    co[9]=co[9] + 1

for i in range(0,n):
    if (numeros[i] >= 0 and numeros[i] <= 999):
        co[0]=co[0] + 1
    elif (numeros[i] >= 1000 and numeros[i] <= 1999):
        co[1]=co[1] + 1
    elif (numeros[i] >= 2000 and numeros[i] <= 2999):
        co[2]=co[2] + 1
    elif (numeros[i] >= 3000 and numeros[i] <= 3999):
        co[3]=co[3] + 1
    elif (numeros[i] >= 4000 and numeros[i] <= 4999):
        co[4]=co[4] + 1
    elif (numeros[i] >= 5000 and numeros[i] <= 5999):
        co[5]=co[5] + 1
    elif (numeros[i] >= 6000 and numeros[i] <= 6999):
        co[6]=co[6] + 1
    elif (numeros[i] >= 7000 and numeros[i] <= 7999):
        co[7]=co[7] + 1
    elif (numeros[i] >= 8000 and numeros[i] <= 8999):
        co[8]=co[8] + 1
    elif (numeros[i] >= 9000 and numeros[i] <= 9999):
        co[9]=co[9] + 1

# df = pd.Series(numeros).value_counts() 
# print(df) 

# print("suma: ",sum(df))

# print("chi cuadrado: ",stats.chisquare(f_obs =co))

# print(co)

def chi_cuadrado(co):
    for i in range(0,10):
        print('Calculo para', i, ((co[i] - 100)**2)/100)

chi_cuadrado(co)


ngraf = []
apyt = []

for i in range(0,n):
    ngraf.insert(i, numeros[i])
    apyt.insert(i, random.randrange(0, 9999, 1))

x=np.arange(0,n,1)
pyplot.figure('ACM')
pyplot.scatter(x, ngraf)
pyplot.figure('RANDOM Python')
pyplot.scatter(x, apyt)
pyplot.show()

