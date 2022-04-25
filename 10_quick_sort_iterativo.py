from time import time
import tracemalloc

from downloads.emp10mil import empresas
#from downloads.emp25mil import empresas
#from downloads.emp50mil import empresas
#from downloads.emp100mil import empresas

passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    """
        Função que implementa o algoritmo Quick Sort de forma ITERATIVA
    """

    if fim is None: fim = len(lista) - 1
    global passadas, comps, trocas

    

    # Cria uma lista auxiliar
    tamanho = fim - ini + 1
    aux = [None] * tamanho
  
    # Inicializa a posição da lista auxiliar
    pos = -1
  
    # Coloca os valores iniciais de ini e fim na lista auxiliar
    pos = pos + 1
    aux[pos] = ini
    pos = pos + 1
    aux[pos] = fim
  
    # Continua retirando valores da lista auxiliar enquanto
    # ela não estiver vazia
    while pos >= 0:
        passadas += 1
        

        # print(aux)
  
        # Retira fim e início
        fim = aux[pos]
        pos = pos - 1
        ini = aux[pos]
        pos = pos - 1
  
        # Coloca o pivô em sua posição correta na lista ordenada
        i = ini - 1
        x = lista[fim]
    
        for j in range(ini , fim):
            if lista[j] <= x:
                comps += 1
                # Incrementa a posição do menor elemento
                i = i + 1
                lista[i], lista[j] = lista[j], lista[i]
    
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        
        pivot = i + 1
  
        # Se há elementos à esquerda do pivô, coloca-os
        # no lado esquerdo da lista auxiliar
        if pivot - 1 > ini:
            trocas += 1
            pos = pos + 1
            aux[pos] = ini
            pos = pos + 1
            aux[pos] = pivot - 1
  
        # Se há elementos à direita do pivô, coloca-os
        # no lado direito da lista auxiliar
        if pivot + 1 < fim:
            trocas += 1
            pos = pos + 1
            aux[pos] = pivot + 1
            pos = pos + 1
            aux[pos] = fim

########################################################################

passadas = comps = trocas = 0

hora_ini = time()
tracemalloc.start() # Inicia o monitoramento da memória

quick_sort(empresas)

# Captura as estatísticas de uso da memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()

# print(nomes[:100]) # Imprime só os 100 primeiros nomes

print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"Passadas: {passadas}, comparações: {comps}, trocas: {trocas}")