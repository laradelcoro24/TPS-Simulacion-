from numpy import number
import pandas as pd
import scipy.stats as stats
from matplotlib import pyplot
import numpy as np
import random

m = 2**48
c = 11
a = 25214903917
x = 2025
n = 1000

numbers=[]
co=[0,0,0,0,0,0,0,0,0,0]

numbers.insert(0, x)
if (numbers[0] >= 0 and numbers[0] <= 999):
    co[0]=co[0] + 1
elif (numbers[0] >= 1000 and numbers[0] <= 1999):
    co[1]=co[1] + 1
elif (numbers[0] >= 2000 and numbers[0] <= 2999):
    co[2]=co[2] + 1
elif (numbers[0] >= 3000 and numbers[0] <= 3999):
    co[3]=co[3] + 1
elif (numbers[0] >= 4000 and numbers[0] <= 4999):
    co[4]=co[4] + 1
elif (numbers[0] >= 5000 and numbers[0] <= 5999):
    co[5]=co[5] + 1
elif (numbers[0] >= 6000 and numbers[0] <= 6999):
    co[6]=co[6] + 1
elif (numbers[0] >= 7000 and numbers[0] <= 7999):
    co[7]=co[7] + 1
elif (numbers[0] >= 8000 and numbers[0] <= 8999):
    co[8]=co[8] + 1
elif (numbers[0] >= 9000 and numbers[0] <= 9999):
    co[9]=co[9] + 1

for i in range(1,n):
    aux = (a * numbers[i-1] + c) % m
    l = len(str(aux))
    numbers.insert(i, int(str(aux)[l-4:l]))
    if (numbers[i] >= 0 and numbers[i] <= 999):
        co[0]=co[0] + 1
    elif (numbers[i] >= 1000 and numbers[i] <= 1999):
        co[1]=co[1] + 1
    elif (numbers[i] >= 2000 and numbers[i] <= 2999):
        co[2]=co[2] + 1
    elif (numbers[i] >= 3000 and numbers[i] <= 3999):
        co[3]=co[3] + 1
    elif (numbers[i] >= 4000 and numbers[i] <= 4999):
        co[4]=co[4] + 1
    elif (numbers[i] >= 5000 and numbers[i] <= 5999):
        co[5]=co[5] + 1
    elif (numbers[i] >= 6000 and numbers[i] <= 6999):
        co[6]=co[6] + 1
    elif (numbers[i] >= 7000 and numbers[i] <= 7999):
        co[7]=co[7] + 1
    elif (numbers[i] >= 8000 and numbers[i] <= 8999):
        co[8]=co[8] + 1
    elif (numbers[i] >= 9000 and numbers[i] <= 9999):
        co[9]=co[9] + 1

# print(numbers)

# df = pd.Series(numbers).value_counts() 
# print(df) 

# print(sum(df))

# print(stats.chisquare(f_obs =co))

# print(co)

def chi_cuadrado(co):
    for i in range(0,10):
        print('Calculo para', i, ((co[i] - 100)**2)/100)

chi_cuadrado(co)



ngraf = []
apyt = []

for i in range(0,n):
    ngraf.insert(i, numbers[i])
    apyt.insert(i, random.randrange(0, 9999, 1))

x=np.arange(0,n,1)
pyplot.figure('GCL',edgecolor='green')
pyplot.scatter(x, ngraf)
pyplot.figure('RANDOM Python',edgecolor='green')
pyplot.scatter(x, apyt)
pyplot.show()