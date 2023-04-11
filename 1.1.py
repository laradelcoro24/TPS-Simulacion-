import numpy as np
import matplotlib.pyplot as plt


n = 10000
n2 = 37

x = np.random.randint(n2)

array_resultados = []
array_frecuencia = [0]
array_promedio = [0]
array_desvio = [0]
array_varianza = [0]
c = 0

for i in range(n):
    random_n = np.random.randint(n2)
    array_resultados.append(random_n)
    media = np.mean(array_resultados)
    array_promedio.append(media)
    desvio = abs(media - x)
    array_desvio.append(desvio)
    varianza = np.var(array_resultados)
    array_varianza.append(varianza)
    if random_n == x:
        c += 1
    array_frecuencia.append(c/(i+1))




plt.plot(array_promedio, color = 'red', label = 'vpn (valor promedio de las tiradas)')
p_esp = (n2 - 1)/2 #promedio esperado
plt.axhline(p_esp, color = 'yellow', label = 'vpe (valor promedio esperado)')
plt.xlabel('n (número de tiradas)')
plt.ylabel('vp (valor promedio de las tiradas)')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.legend()
plt.show()

plt.plot(array_desvio, color = 'red', label = 'vd (valor del desvío del número X)')
d_esp = abs(p_esp - x) #desvio esperado
plt.axhline(d_esp, color = 'yellow', label = 'vde (valor del desvío esperado)')
plt.xlabel('n (número de tiradas)')
plt.ylabel('vd (valor del desvío)')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.legend()
plt.show()

plt.plot(array_varianza, color = 'red', label = 'vv (valor de la varianza obtenida)')
v_esp = (n2 ** 2 -1) / 12 #varianza esperada
plt.axhline(v_esp, color = 'yellow', label = 've (valor de la varianza esperada)')
plt.xlabel('n (número de tiradas)')
plt.ylabel('vv (valor de la varianza)')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.legend()
plt.show()

plt.plot(array_frecuencia, color = 'red', label = 'frn (frecuencia relativa del número x con respecto a n)')
f_esp = 1/(n2) #frecuencia esperada
plt.axhline(f_esp, color = 'yellow', label = 'fre (frecuencia relativa esperada de X)')
plt.xlabel('n (número de tiradas)')
plt.ylabel('fr (frecuencia relativa)')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.legend()
plt.show()