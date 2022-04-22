# ALGORITMO DE ORDENAÇÃO BUBBLE SORT
#
# Percorre a lista a ser ordenada em sucessivas passadas,
# trocando elementos adjacentes entre si quando o segundo for
# menor que o primeiro. Efetua tantas passadas quanto necessárias
# até que, na última passada, nenhuma troca seja efetuada.

from data.nomes_desord import nomes
from time import time
import tracemalloc

# from downloads.emp10mil import empresas
#from downloads.emp25mil import empresas
from downloads.emp50mil import empresas
# from downloads.emp100mil import empresas

passadas = comps = trocas = 0

def bubble_sort(lista):

    # Declara o uso de variáveis globais
    global passadas, comps, trocas
    passadas = comps = trocas = 0

    # Loop eterno (não sabemos quantas passadas serão necessárias)
    while True:
        passadas += 1
        trocou = False  # Controla se houve ou não trocas
        # Percurso da lista da primeira até a PENÚLTIMA posição
        for pos in range(len(lista) - 1):
            comps += 1
            if lista[pos] > lista[pos + 1]:
                # Troca os elementos de posição
                lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos]
                trocou = True
                trocas += 1

        # Se não houve trocas, interrompe o loop de passadas
        if not trocou:
            break

########################################################################        


nums = [7, 4, 2, 9, 0, 6, 8, 3, 1, 5]

hora_ini = time()
tracemalloc.start()

bubble_sort(empresas)

mem_atual, mem_pico = tracemalloc.get_traced_memory()
hora_fim = time()

print(f"Tempo gasto para ordenar: {(hora_fim - hora_ini) * 1000}ms")
print(f"Pico de memória: { mem_pico / 1024 / 1024 } MB")
print(f"passadas: {passadas}, comparações: {comps}, trocas: {trocas}")




