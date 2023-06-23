import numpy as np
import matplotlib.pyplot as plt

#PARÁMETROS
tasa_servicio = 25 # personas/minuto. 
tasa_arribo = tasa_servicio * 0.25 #personas/minuto . Variar 0.25, 0.5, 0.75, 1, 1.25
cantidad_corridas = 10 
total_clientes = 5000  # fin de la simulacion 

#Variables e inicialización
cant_tipo_evento = 2  # tipos de eventos (arribos y llegadas)
time = 0.0  # reloj de simulación
b_estado_servidor = 0  # B(t) = 0: servidor libre - 1: servidor ocupado
q_ncc = 0  # número de clientes en cola Q(t)
area_bajo_q = 0.0  
area_bajo_b = 0.0 
tiempo_ultimo_evento = 0.0 
num_clientes = 0 # número de clientes que completaron su demora en cola
arreglo_prox_evento = np.zeros([cant_tipo_evento + 1]) # arreglo que contiene el tiempo del próximo evento I en la posición ARREGLO_PROX_EV[I]
demora_total = 0.0 # tiempo total de los clientes que completaron sus demoras
tiempo_prox_evento = 0.0 
tipo_prox_evento = 0 # tipo del proximo evento (1: ARRIBOS o 2: PARTIDAS) 
arreglo_tiempos_arribo = np.zeros([total_clientes + 1]) # tiempo de arribo del cliente I que está esperando en cola
tiempo_servicio_acumulado = 0.0
util_corridas, demora_cola_corridas, clientes_cola_corridas, demora_sistema_corridas, clientes_sistema_corridas, contq_ncc, probq_ncc = [], [], [], [], [], [0] * total_clientes, []


def timing():
    global time,arreglo_prox_evento, tipo_prox_evento, tiempo_prox_evento, cant_tipo_evento
    tiempo_prox_evento = 1e29
    tipo_prox_evento = 0
    for i in range(1, cant_tipo_evento + 1):
        if arreglo_prox_evento[i] <tiempo_prox_evento:
            tiempo_prox_evento = arreglo_prox_evento[i]
            tipo_prox_evento = i
    if tipo_prox_evento >0:
        time = tiempo_prox_evento
        return 0
    else:
        print('Lista de eventos vacias. Fin de la simulacion')
        return 1

def arribo():
    global b_estado_servidor,demora_total,num_clientes,arreglo_tiempos_arribo,arreglo_prox_evento, tiempo_ultimo_evento, tiempo_servicio_acumulado, area_bajo_q, q_ncc 
    arreglo_prox_evento[1] = time + np.random.exponential(1 / tasa_arribo)
    if b_estado_servidor == 1:
        area_bajo_q += q_ncc * (time - tiempo_ultimo_evento)
        tiempo_ultimo_evento = time
        q_ncc += 1
        if q_ncc <= total_clientes:
            arreglo_tiempos_arribo[q_ncc] = time
        else:
            print('Se alcanzó el limite de clientes a observar')
    else:
        DEMORA = 0.0
        b_estado_servidor = 1
        demora_total += DEMORA
        num_clientes += 1
        arreglo_prox_evento[2] = time + np.random.exponential(1 / tasa_servicio)
        tiempo_servicio_acumulado += (arreglo_prox_evento[2] - time)

def partida():
    global q_ncc, b_estado_servidor, area_bajo_q, time, tiempo_ultimo_evento, arreglo_tiempos_arribo, demora_total,arreglo_prox_evento, DEMORA, num_clientes, tasa_servicio, tiempo_servicio_acumulado
    if q_ncc > 0:
        area_bajo_q += q_ncc * (time - tiempo_ultimo_evento)
        tiempo_ultimo_evento = time
        q_ncc -= 1
        DEMORA = time - arreglo_tiempos_arribo[1]
        demora_total += DEMORA
        num_clientes += 1
        arreglo_prox_evento[2] = time + np.random.exponential(1 / tasa_servicio)
        tiempo_servicio_acumulado += (arreglo_prox_evento[2] - time)
    if q_ncc != 0:
        for i in range(1, q_ncc + 1):
            arreglo_tiempos_arribo[i]=arreglo_tiempos_arribo[i+1]
    else:
        b_estado_servidor = 0
        arreglo_prox_evento[2] = 10.0 ** 30 
    return None

def report():
    global total_clientes, num_clientes, area_bajo_q, demora_total, time, tiempo_servicio_acumulado
    print("Promedio de clientes en el sistema: " , round((num_clientes / time), 3))
    print('Promedio de clientes en cola', round((area_bajo_q / time), 3))
    print("Tiempo promedio en el sistema: ", round((demora_total / total_clientes), 3), " minutos")
    print('Tiempo promedio en cola:', round((demora_total / num_clientes), 3), ' minutos')
    print('Utilización del servidor:', "{:.2%}".format(tiempo_servicio_acumulado / time ))

def graficar(muestra, tit, ylbl):
    plt.title(tit)
    plt.xlabel('Corrida')
    plt.ylabel(ylbl)
    plt.bar([x+0.25 for x in range(len(muestra))], muestra, color = "green", width = 0.5)
    plt.xticks([x+0.15 for x in range(len(muestra))], [x for x in range(len(muestra))])
    plt.show()

def grafico_probNegacion_probNclientes(probabilidad1):
    n_clientes_observados, probs2 = [], []
    n_clientes_observados.append(1 - probabilidad1[0])
    for j in [0, 2, 5, 10, 50]: #probabilidad de denegacion de servicio para cola finita de tamaño 0, 2, 5 ,10, 50
        n_clientes_observados.append(1 - sum(probabilidad1[i] for i in range(j)))

    print("Probabilidad de denegación de servicio:", n_clientes_observados)
    for i in range(len(probabilidad1)):
        if probabilidad1[i] > 0:
            probs2.append(probabilidad1[i])
    
    #grafico probabilidad de N clientes en cola
    plt.subplot(121)
    plt.title("Probabilidad de N clientes en cola")
    plt.xlabel('Numero de clientes')
    plt.ylabel("Probabilidad")
    plt.bar([x + 0.25 for x in range(len(probs2))], probs2, color="orange", width=0.5)
    plt.xticks([x + 0.15 for x in range(len(probs2))], [x for x in range(len(probs2))])
    plt.legend(loc='upper right')

    #grafico probabilidad de denegacion
    plt.subplot(122)
    plt.title("Probabilidad de denegación de servicio")
    plt.xlabel('Tamaño de la cola')
    plt.ylabel('Probabilidad')
    plt.bar([x + 0.25 for x in range(len(n_clientes_observados))], n_clientes_observados, color="orange")
    plt.xticks([0, 1, 2, 3, 4], labels=['0', '2', '5', '10', '50'])
    #plt.xscale({'0', '2', '5', '10', '50'})
    plt.show()



#MAIN

for i in range(cantidad_corridas):
 
    b_estado_servidor = 0 
    q_ncc = 0
    num_clientes = 0
    tipo_prox_evento = 0
    time = 0.0 
    tiempo_ultimo_evento = 0.0 
    demora_total = 0.0 
    area_bajo_q = 0.0 
    area_bajo_b = 0.0 
    tiempo_servicio_acumulado = 0.0 
    tiempo_prox_evento=0.0     
    arreglo_prox_evento = np.zeros([cant_tipo_evento + 1]) 
    arreglo_tiempos_arribo = np.zeros([total_clientes + 1]) 
    arreglo_prox_evento[1] = time + np.random.exponential(1 / tasa_arribo)
    arreglo_prox_evento[2] = 1e30 

    while num_clientes <= total_clientes:
        timing()
        if timing() == 0:
            time_since_last_event = time - tiempo_ultimo_evento
            tiempo_ultimo_evento = time
            area_bajo_q = area_bajo_q + (q_ncc * time_since_last_event)
            area_bajo_b = area_bajo_b + (b_estado_servidor * time_since_last_event)
            if tipo_prox_evento == 1:
                arribo()
            else:
                contq_ncc[q_ncc] +=1 
                partida()
        elif timing() == 1:
            break
    print("\n\n ----- Corrida nº: ", i+1, " ----- ")
    report()

    clientes_sistema_corridas.append(tasa_arribo * ((demora_total / num_clientes) + (1 / tasa_servicio)))
    clientes_cola_corridas.append((area_bajo_q / time))
    demora_sistema_corridas.append((demora_total / num_clientes) + (1 / tasa_servicio))
    demora_cola_corridas.append(demora_total / num_clientes)
    util_corridas.append(area_bajo_b / time)


for j in range(len(contq_ncc)):
    probq_ncc.append(contq_ncc[j]/sum(contq_ncc))
print("\n\n ----- Promedios generales de todas las corridas: -----")
print("Numero de clientes en el sistema:", round(np.mean(clientes_sistema_corridas), 3))
print("Numero de clientes en cola:", round(np.mean(clientes_cola_corridas), 3))
print("Tiempo promedio en el sistema:", round(np.mean(demora_sistema_corridas), 3))
print("Tiempo promedio en cola:", round(np.mean(demora_cola_corridas), 3))
print("Utilizacion del servidor: ","{:.2%}".format(np.mean(util_corridas)))
print("\n") 
for j in range(len(probq_ncc)):
    if probq_ncc[j] > 0:
       print('Probabilidad de que haya {0} clientes en cola: {1}%'.format(j, round((probq_ncc[j]*100),2))) 


graficar(clientes_sistema_corridas, 'Clientes promedio en el sistema', 'S(t)')
graficar(clientes_cola_corridas, 'Clientes promedio en cola', 'Q(t)')
graficar(demora_sistema_corridas, 'Demora promedio en el sistema', 'Ds(n)')
graficar(demora_cola_corridas, 'Demora promedio en cola', 'Dq(n)')
graficar(util_corridas, 'Utilización del servidor', 'B(t)')
grafico_probNegacion_probNclientes(probq_ncc)

