# Desenvolvido por:
#   Diogo Silveira dos Santos
#   João Vitor Izael Souza
#   João Vitor Oliveira de Melo
#   Luiz Otávio de Oliveira Silva
#   Pedro Henrique Carreto Morais

import random
import time
from datetime import datetime

def two_generals():
    # Obtenção e exibição do horário do início
    time_init = datetime.now()
    print("Hora de inicio: "+str(time_init.hour)+':' + str(time_init.minute)+":"+str(time_init.second))

    # Inicialização de variáveis
    vermelho_mensageiro, azul_mensageiro = 0, 0
    tempoVermelho, tempoAzul, time_elapsed, time_imp = [], [], [], []
    everReached, capt = 0, 1

    while(True):
        # Verifica se existem mensageiros restantes
        if (verMensageiro(vermelho_mensageiro, azul_mensageiro) != 0):
            return verMensageiro(vermelho_mensageiro, azul_mensageiro), time_elapsed

        if (tempoVermelho == []):
            # Envia um mensageiro vermelho e verifica se foi capturado
            time_elapsed, vermelho_mensageiro, tempoVermelho = enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho)
            capturou, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 0)

            if (capturou == 0):
                # Chega no Azul
                imp, time_elapsed, azul_mensageiro = chegaNoAzul(time_elapsed, azul_mensageiro)
                if (imp == 0):
                    everReached = 1
                else:
                    while (sum(time_imp) < 12600):
                        time_elapsed, azul_mensageiro, tempoAzul = enviaAzul(time_elapsed, azul_mensageiro, tempoAzul)
                        voltou, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 1)
                        if (voltou == 0):
                            # Não foi capturado no retorno da impossibilitação
                            time_imp.append(12600)
                            print("Sinalizador disparado da impossibilitação")
                        else:
                            time_imp.append(random.randint(3600, 4201))
                    time_imp = []

        if (everReached == 1):
            if (tempoAzul == []):
                # Envia um mensageiro azul e verifica se foi capturado
                time_elapsed, azul_mensageiro, tempoAzul = enviaAzul(time_elapsed, azul_mensageiro, tempoAzul)
                capt, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 1)
            if (capt == 0):
                # Não foi capturado, logo o sinalizador foi disparado
                return 0, time_elapsed
            if (capt == 1 or sum(tempoAzul) > 4200):
                tempoAzul = []

        if (sum(tempoVermelho) > 12600 or everReached == 0):
            tempoVermelho = []


# Verifica a existência de mensageiros
def verMensageiro(vermelho_mensageiro, azul_mensageiro):
    if (vermelho_mensageiro == 5):
        return 1

    if (azul_mensageiro == 10):
        return 2

    return 0


# Envia um mensageiro vermelho
def enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho):
    if (vermelho_mensageiro == 5):
        return time_elapsed, vermelho_mensageiro, tempoVermelho

    vermelho_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))

    print("Enviando mensageiro vermelho", 5-vermelho_mensageiro, "restantes")
    return time_elapsed, vermelho_mensageiro, tempoVermelho


# Realiza a verificação randômica de captura de travessia
def tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, azul):
    tentativa = random.randint(1, 101)
    tempoDecorrido = random.randint(3600, 4201)
    tempoVermelho.append(tempoDecorrido)

    if (azul == 1):
        tempoAzul.append(tempoDecorrido)

    if (tentativa <= 45):
        print("Castelo Capturou!")
        time_elapsed.append(12600 + 1)
        return 1, time_elapsed, tempoVermelho, tempoAzul
    else:
        print("Castelo nao Capturou!")
        return 0, time_elapsed, tempoVermelho, tempoAzul


# Verifica se o azul aceita o horário proposto
def chegaNoAzul(time_elapsed, azul_mensageiro):
    negar = random.randint(1, 101)

    if(negar == 1):
        print("Exercito azul impossibilitou o horário!")
        return 1, time_elapsed, azul_mensageiro
    else:
        print("Exercito azul aceita o horário!")
        return 0, time_elapsed, azul_mensageiro


# Envia um mensageiro azul
def enviaAzul(time_elapsed, azul_mensageiro, tempoAzul):
    azul_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))

    print("Enviando mensageiro azul", 10-azul_mensageiro, "restantes")
    return time_elapsed, azul_mensageiro, tempoAzul


# Transforma segundos para horas, minutos e segundos
def seg_toDateTime(s):
    s = s % (24 * 3600 * 60)
    s %= 216000
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    return hour, minutes, s


# Inicia o problema
problem, time_elapsed = two_generals()

# Verifica as saidas obtidas
if problem == 0:
    print("\nSinalizador disparado")

if problem == 1:
    print("\nVermelho sem mensageiros")

if problem == 2:
    print("\nAzul sem mensageiros")

# Elimina contagens de tempo inválidas
for i in range(0, len(time_elapsed)):
    try:
        if (time_elapsed[i+1] == 12600):
            time_elapsed[i] = 0
    except:
        None

# Define e exibe os timestamps
time_stamp_inicial = time.time()
time_stamp_final = time_stamp_inicial + sum(time_elapsed)

hour, minutes, s = seg_toDateTime(sum(time_elapsed))

print("Tempo decorrido: %02d:%02d:%02d" % (hour, minutes, s))
print("\nTimestamp Inicial: %.0f" % (time_stamp_inicial))
print("Timestamp Final: %.0f" % (time_stamp_final))
