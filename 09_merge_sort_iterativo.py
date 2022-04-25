

from time import time
import tracemalloc

#from downloads.emp10mil import empresas
#from downloads.emp25mil import empresas
#from downloads.emp50mil import empresas
from downloads.emp100mil import empresas


def merge_sort(lista):
    """
        Função que implementa o algoritmo Merge Sort de forma ITERATIVA
    """

    # Inicia com o menor tamanho de partição de 2^0 = 1
    tam_part = 1
    n = len(lista)
    
    # O tamanho da sublista cresce em potências de 2
    while (tam_part < n):
        # Inicia sempre pela esquerda
        esq = 0
        while (esq < n):
            dir = min(esq + (tam_part * 2 - 1), n - 1)
            meio = (esq + dir)//2

            # print(f"esq: {esq}, dir: {dir}, meio: {meio}")

            # A mescla final deve considerar sublistas
            # não mescladas se o tamannho da lista original
            # não for potência de 2
            if (tam_part > n//2):
                meio = dir  - (n % tam_part)
            
            tam_esq = meio - esq + 1
            tam_dir = dir - meio
            lista_esq = [0] * tam_esq   # Vetor auxiliar
            lista_dir = [0] * tam_dir   # Vetor auxiliar
            for pos_esq in range(0, tam_esq):
                lista_esq[pos_esq] = lista[esq + pos_esq]
            for pos_esq in range(0, tam_dir):
                lista_dir[pos_esq] = lista[meio + pos_esq + 1]

            pos_esq, pos_dir, i = 0, 0, esq
            while pos_esq < tam_esq and pos_dir < tam_dir:
                if lista_esq[pos_esq] > lista_dir[pos_dir]:
                    lista[i] = lista_dir[pos_dir]
                    pos_dir += 1
                else:
                    lista[i] = lista_esq[pos_esq]
                    pos_esq += 1
                i += 1

            while pos_esq < tam_esq:
                lista[i] = lista_esq[pos_esq]
                pos_esq += 1
                i += 1

            while pos_dir < tam_dir:
                lista[i] = lista_dir[pos_dir]
                pos_dir += 1
                i += 1

            esq += tam_part * 2
        # Incrementa a sublista em potências de 2
        tam_part *= 2
    return lista

############################################################

hora_ini = time()
tracemalloc.start() # Inicia o monitoramento da memória

nomes_ord = merge_sort(empresas)

# Captura as estatísticas de uso da memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()


print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")