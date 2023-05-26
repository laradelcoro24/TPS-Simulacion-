import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from collections import Counter

#Genera un número con distribución uniforme
def RNG_uniforme(a = 0, b = 1):
    r = np.random.rand()
    x = r * (b - a) + a
    return x

#Genera una serie de números aleatorios con distribución uniforme
def uniforme_rand(n, a= 0, b = 1):
    c = b - a
    serie = np.random.rand(n) * c + a
    return serie

#Genera un número con distribución exponencial
def RNG_exponencial(p_lambda = 1):
    r = np.random.rand()
    x = - np.log(r) / p_lambda
    return x

#Genera una serie de números aleatorios con distribución exponencial
def exponencial_rand(n, p_lambda = 1):
    serie = - np.log(np.random.rand(n)) / p_lambda
    return serie

#Genera un número con distribución gamma
def RNG_gamma(k = 1, alpha = 1):
    productoria = np.prod(np.random.rand(k))
    x = - np.log(productoria) / alpha
    return x

#Genera una serie de números aleatorios con distribución gamma
def gamma_rand(n, k =1, alpha = 1):
    serie = np.empty(n)
    for i in range(n):
        serie[i] = RNG_gamma(k, alpha)
    return serie

#Genera un número con distribución normal
def RNG_normal(mu = 0, sigma = 1, K = 24):
    sumatoria = np.sum(np.random.rand(K))
    x = sigma * (12 / K) ** 0.5 * (sumatoria - K/2) + mu
    return x

#Genera una serie de números aleatorios con distribución normal
def normal_rand(n, mu = 0, sigma = 1, K = 24):
    a = (12 / K) ** 0.5
    b = K/2
    serie = np.empty(n)
    for i in range(n):
        sum = np.sum(np.random.rand(K))
        serie[i] = sigma * a * (sum - b) + mu
    return serie

#Genera un número con distribución binomial
def RNG_binomial(param_n, p):
    x = 0
    for i in range(param_n):
        if np.random.rand() < p:
            x += 1
    return x

#Genera una serie de números aleatorios con distribución binomial
def binomial_rand(n, param_n, p):
    serie = np.empty(n)
    for i in range(n):
        serie[i] = RNG_binomial(param_n, p)
    return serie

#Genera un número con distribución de Pascal
def RNG_pascal(r, p):
    log_q = np.log(1-p)
    productoria = np.prod(np.random.rand(r))
    x = np.log(productoria) / log_q
    x = np.floor(x)
    return x

#Genera una serie de números aleatorios con distribución de Pascal
def pascal_rand(n, r, p):
    log_q = np.log(1-p)
    serie = np.empty(n)
    for i in range(n):
        productoria = np.prod(np.random.rand(r))
        serie[i] = np.log(productoria) / log_q
    serie = np.floor(serie)
    return serie

#Genera un número con distribución hipergeométrica
def RNG_hipergeometrica(N_t, K, n_p):
    x = 0
    for i in range(K):
        r = np.random.rand()
        if r < (n_p/N_t):
            x += 1
            n_p -= 1
        N_t -= 1
    return x

#Genera una serie de números aleatorios con distribución hipergeométrica
def hipergeometrica_rand(n, N_t, K, n_p):
    serie = np.empty(n)
    for i in range(n):
        serie[i] = RNG_hipergeometrica(N_t, K, n_p)
    return serie

#Genera un número con distribución de Poisson
def RNG_poisson(p_lambda = 1):
    x = 0
    exp = np.exp(- p_lambda)
    tr = 1
    tr *= np.random.rand()
    while (exp - tr) < 0:
        x += 1
        tr *= np.random.rand()
    return x

#Genera una serie de números aleatorios con distribución de Poisson
def poisson_rand(n, p_lambda):
    serie = np.empty(n)
    for i in range(n):
        serie[i] = RNG_poisson(p_lambda)
    return serie

#Genera un número con distribución empírica discreta
def RNG_empirica(valores, probabilidades):
    n = np.size(probabilidades)
    prob_acumuladas = np.empty(n)
    prob_acumuladas[0] = probabilidades[0]
    for i in range(n - 1):
        prob_acumuladas[i + 1] = probabilidades[i + 1] + prob_acumuladas[i]
    r = np.random.rand()
    i = 0
    x = valores[i]
    while r > prob_acumuladas[i]:
        i += 1
        x = valores[i]
    return x

#Genera una serie de números aleatorios con distribución empírica discreta
def empirica_rand(n, valores, probabilidades):
    serie = np.empty(n)
    for i in range(n):
        serie[i] = RNG_empirica(valores, probabilidades)
    return serie

def grafico_dispersion(arreglo, label='',titulo=''):
    fig, ax = plt.subplots()
    ax.plot(arreglo,color='Black', marker='o',linestyle = 'None', label=label)
    ax.set_ylabel('valor de n')
    ax.set_xlabel('n')
    ax.set_title(titulo)
    ax.legend()
    fig.savefig(titulo + '_dispersion')
    # plt.show()

def histograma(arreglo, n_columnas=10, titulo='', label='', range='default'):
    if range == 'default':
        range = (np.min(arreglo), np.max(arreglo))
    fig, ax = plt.subplots()
    ax.hist(arreglo, bins=n_columnas, range=range, label=label, rwidth=0.95, color='Black')
    ax.set_ylabel('cantidad de ocurrencias')
    ax.set_xlabel('rango')
    ax.set_title(titulo)
    ax.legend()
    fig.savefig(titulo + '_histograma')
    # plt.show()

def hist_varios(series, labels, titulo, n_bins = 25):
    fig, ax = plt.subplots()
    for i in range(np.size(series, 0)):
        ax.hist(series[i], bins=n_bins, histtype='step', label=labels[i], density=True)
    ax.set_title(titulo)
    ax.legend()
    ax.set_ylabel('porcentaje de ocurrencias')
    ax.set_xlabel('rango')
    fig.savefig(titulo + '_hist_varios')
    # plt.show()

def hist_compara(serie1, distribucion, titulo='', n_bins1 = 25, label=''):
    fig, ax = plt.subplots()
    ax.hist(serie1, bins=n_bins1, label=label, color='LightBlue', density=True)
    x = np.linspace(min(serie1), max(serie1), 100)
    ax.plot(x, distribucion.pdf(x), label='Distribución esperada', color='Red')
    ax.set_title(titulo[:-1])
    ax.legend()
    ax.set_ylabel('porcentaje de ocurrencias')
    ax.set_xlabel('rango')
    fig.savefig(titulo + '_test')
    # plt.show()

def hist_compara_discreta(serie1, distribucion, titulo='', label=''):
    fig, ax = plt.subplots()
    counter = Counter(serie1)
    ax.bar(counter.keys(), counter.values(), 0.1, label=label, color='LightBlue')
    x = np.arange(min(serie1), max(serie1) + 1, 1)
    ax.plot(x, distribucion.pmf(x) * np.size(serie1), 'ro', label='Distribución esperada')
    ax.set_title(titulo[:-1])
    ax.legend()
    ax.set_ylabel('cantidad de ocurrencias')
    ax.set_xlabel('numero')
    fig.savefig(titulo + '_test')
    # plt.show()

def hist_compara_empirica(serie1, valores, probabilidades, titulo='', label=''):
    fig, ax = plt.subplots()
    counter = Counter(serie1)
    ax.bar(counter.keys(), counter.values(), 0.1, label=label, color='LightBlue')
    probabilidades = np.array(probabilidades) * np.size(serie1)
    ax.plot(valores, probabilidades, 'ro', label='Distribución esperada')
    ax.set_title(titulo[:-1])
    ax.legend()
    ax.set_ylabel('cantidad de ocurrencias')
    ax.set_xlabel('numero')
    fig.savefig(titulo + '_test')
    # plt.show()

# Distribución uniforme
serie_aleatoria = uniforme_rand(3000, 2, 20)
label = r'a = 2, b = 20'
grafico_dispersion(serie_aleatoria, titulo='Distribución uniforme', label=label)
histograma(serie_aleatoria, titulo='Distribución uniforme', label=label)
parametros = [(0,5),(0,10),(3,9)]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(uniforme_rand(3000, parametros[i][0], parametros[i][1]))
    labels.append('a = ' + str(parametros[i][0]) + ', b = ' + str(parametros[i][1]))
hist_varios(series, labels, 'Distribución uniforme', 10)

# Distribución exponencial
serie_aleatoria = exponencial_rand(3000, 1)
label = r'$\lambda = 1$'
grafico_dispersion(serie_aleatoria, titulo='Distribución exponencial', label=label)
histograma(serie_aleatoria, titulo='Distribución exponencial', label=label)
parametros = [0.5,1,2]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(exponencial_rand(3000, parametros[i]))
    labels.append(r'$\lambda = $' + str(parametros[i]))
hist_varios(series, labels, 'Distribución exponencial')

# Distribución gamma
serie_aleatoria = gamma_rand(3000, 5, 1)
label = r'$k = 5, \alpha = 1$'
grafico_dispersion(serie_aleatoria,  titulo='Distribución gamma', label=label)
histograma(serie_aleatoria, titulo='Distribución gamma', label=label)
parametros = [[1,1],[2,0.5],[9,2],[7,1]]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(gamma_rand(3000, parametros[i][0], parametros[i][1]))
    labels.append('k = ' + str(parametros[i][0]) + r'$, \alpha = $' + str(parametros[i][1]))
hist_varios(series, labels, 'Distribución gamma')

# Distribución normal
serie_aleatoria = normal_rand(3000, 0, 1)
label = r'$\mu = 0, \sigma = 1$'
grafico_dispersion(serie_aleatoria,  titulo='Distribución normal', label=label)
histograma(serie_aleatoria, titulo='Distribución normal', label=label)
parametros = [[0,1],[0,0.5],[0,2],[5,1]]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(normal_rand(3000, parametros[i][0], parametros[i][1]))
    labels.append(r'$\mu = $' + str(parametros[i][0]) + r'$, \sigma = $' + str(parametros[i][1]))
hist_varios(series, labels, 'Distribución normal')

# Distribución binomial
serie_aleatoria = binomial_rand(3000, 10, 0.5)
label = 'n = 10, p = 0.5'
grafico_dispersion(serie_aleatoria, titulo='Distribución binomial', label=label)
histograma(serie_aleatoria, titulo='Distribución binomial', label=label)
parametros = [[10,0.5],[10,0.8],[5,0.5]]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(binomial_rand(3000, parametros[i][0], parametros[i][1]))
    labels.append('n = ' + str(parametros[i][0]) + ', p = ' + str(parametros[i][1]))
hist_varios(series, labels, 'Distribución binomial', 6)

# Distribución de Pascal
serie_aleatoria = pascal_rand(3000, 10, 0.5)
label = 'k = 10, p = 0.5'
grafico_dispersion(serie_aleatoria, titulo='Distribución de Pascal', label=label)
histograma(serie_aleatoria, 10, titulo='Distribución de Pascal', label=label)
parametros = [[10,0.3],[10,0.7],[15,0.5],[5,0.5]]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(pascal_rand(3000, parametros[i][0], parametros[i][1]))
    labels.append('k = ' + str(parametros[i][0]) + ', p = ' + str(parametros[i][1]))
hist_varios(series, labels, 'Distribución de Pascal', 10)

# Distribución hipergeométrica
serie_aleatoria = hipergeometrica_rand(3000, 500, 60, 200)
label = 'N = 500, K = 60, n = 200'
grafico_dispersion(serie_aleatoria, titulo='Distribución hipergeométrica', label=label)
histograma(serie_aleatoria, 10, titulo='Distribución hipergeométrica', label=label)
parametros = [[500,60,200],[500,30,200],[500,60,100]]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(hipergeometrica_rand(3000, parametros[i][0], parametros[i][1], parametros[i][2]))
    labels.append('N = ' + str(parametros[i][0]) + ', K = ' + str(parametros[i][1]) + ', n = ' + str(parametros[i][2]))
hist_varios(series, labels, 'Distribución hipergeométrica', 10)

# Distribución de Poisson
serie_aleatoria = poisson_rand(3000, 1)
label = r'$\lambda = 1$'
grafico_dispersion(serie_aleatoria, titulo='Distribución de Poisson', label=label)
histograma(serie_aleatoria, 6, titulo='Distribución de Poisson', label=label)
parametros = [0.5,1,2,4]
series = []
labels = []
for i in range(np.size(parametros, 0)):
    series.append(poisson_rand(3000, parametros[i]))
    labels.append(r'$\lambda = $' + str(parametros[i]))
hist_varios(series, labels, 'Distribución de Poisson', 7)

# Distribución empírica discreta
valores = [1, 2 ,3 ,4 , 5, 6]
probabilidades = [0.3, 0.05, 0.2, 0.1, 0.3, 0.05]
serie_aleatoria = empirica_rand(3000, valores, probabilidades)
label = 'p(1) = 0.3, p(2) = 0.05, p(3) = 0.2, p(4) = 0.1, p(5) = 0.3, p(6) = 0.05'
grafico_dispersion(serie_aleatoria, titulo='Distribución empírica discreta', label=label)
histograma(serie_aleatoria, 6, titulo='Distribución empírica discreta', label=label)
lista_valores = [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[2, 3, 7]]
lista_probabilidades = [[0.05, 0.1, 0.2, 0.3, 0.35],[0.5, 0.1, 0.1, 0.1, 0.2],[0.2, 0.5, 0.3]]
series = []
labels = []
for i in range(np.size(lista_valores, 0)):
    series.append(empirica_rand(3000, lista_valores[i], lista_probabilidades[i]))
    label = ''
    for j in range(np.size(lista_valores[i])):
        label = label + 'p(' + str(lista_valores[i][j]) + ') = ' + str(lista_probabilidades[i][j]) + ', '
    labels.append(label[:-2])
hist_varios(series, labels, 'Distribución empírica discreta', 5)

#Test distribución uniforme
parametros = [[0,10],[5,8],[1,4]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = uniforme_rand(3000, parametros[i][0], parametros[i][1])
    label = 'a = ' + str(parametros[i][0]) + ', b = ' + str(parametros[i][1])
    distribucion = stats.uniform(loc=parametros[i][0], scale=parametros[i][1] - parametros[i][0])
    hist_compara(serie_aleatoria, distribucion, titulo='Distribución uniforme' + str(i), label=label)

#Test distribución exponencial
parametros = [1,0.5,3]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = exponencial_rand(3000, parametros[i])
    label = r'$\lambda = $' + str(parametros[i])
    distribucion = stats.expon(scale=1 / parametros[i])
    hist_compara(serie_aleatoria, distribucion, titulo='Distribución exponencial' + str(i), label=label)

#Test distribución gamma
parametros = [[2,1],[9,1],[7,1]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = gamma_rand(3000, parametros[i][0], parametros[i][1])
    label = 'k = ' + str(parametros[i][0]) + r'$, \alpha = $' + str(parametros[i][1])
    distribucion = stats.gamma(parametros[i][0], scale = 1 / parametros[i][1])
    hist_compara(serie_aleatoria, distribucion, titulo='Distribución gamma' + str(i), label=label)

#Test distribución normal
parametros = [[0,1],[0,0.5],[5,1]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = normal_rand(3000, parametros[i][0], parametros[i][1])
    label = r'$\mu = $' + str(parametros[i][0]) + r'$, \sigma = $' + str(parametros[i][1])
    distribucion = stats.norm(loc=parametros[i][0], scale=parametros[i][1])
    hist_compara(serie_aleatoria, distribucion, titulo='Distribución normal' + str(i), label=label)

#Test distribución binomial
parametros = [[10,0.5],[10,0.8],[5,0.5]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = binomial_rand(3000, parametros[i][0], parametros[i][1])
    label = 'n = ' + str(parametros[i][0]) + ', p = ' + str(parametros[i][1])
    distribucion = stats.binom(parametros[i][0], parametros[i][1])
    hist_compara_discreta(serie_aleatoria, distribucion, titulo='Distribución binomial' + str(i), label=label)

#Test distribución de Pascal
parametros = [[10,0.3],[15,0.5],[5,0.5]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = pascal_rand(3000, parametros[i][0], parametros[i][1])
    label = 'k = ' + str(parametros[i][0]) + ', p = ' + str(parametros[i][1])
    distribucion = stats.nbinom(parametros[i][0], parametros[i][1], loc = np.floor(parametros[i][0]/2))
    hist_compara_discreta(serie_aleatoria, distribucion, titulo='Distribución de Pascal' + str(i), label=label)

#Test distribución hipergeométrica
parametros = [[500,60,200],[500,30,200],[500,60,100]]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = hipergeometrica_rand(3000, parametros[i][0], parametros[i][1], parametros[i][2])
    label = 'N = ' + str(parametros[i][0]) + ', K = ' + str(parametros[i][1]) + ', n = ' + str(parametros[i][2])
    distribucion = stats.hypergeom(parametros[i][0], parametros[i][2], parametros[i][1])
    hist_compara_discreta(serie_aleatoria, distribucion, titulo='Distribución hipergeométrica' + str(i), label=label)

#Test distribución de Poisson
parametros = [0.5,1,3]
for i in range(np.size(parametros, 0)):
    serie_aleatoria = poisson_rand(3000, parametros[i])
    label = r'$\lambda = $' + str(parametros[i])
    distribucion = stats.poisson(parametros[i])
    hist_compara_discreta(serie_aleatoria, distribucion, titulo='Distribución de Poisson' + str(i), label=label)

#Test distribución empírica discreta
lista_valores = [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5],[2, 3, 7]]
lista_probabilidades = [[0.05, 0.1, 0.2, 0.3, 0.35],[0.5, 0.1, 0.1, 0.1, 0.2],[0.2, 0.5, 0.3]]
for i in range(np.size(lista_valores, 0)):
    serie_aleatoria = empirica_rand(3000, lista_valores[i], lista_probabilidades[i])
    label = ''
    for j in range(np.size(lista_valores[i])):
        label = label + 'p(' + str(lista_valores[i][j]) + ') = ' + str(lista_probabilidades[i][j]) + ', '
    label = label[:-2]
    hist_compara_empirica(serie_aleatoria, lista_valores[i], lista_probabilidades[i], titulo='Distribución empírica discreta' + str(i), label=label)
