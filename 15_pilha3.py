from lib.stack import Stack

analisador = Stack()

# expr = 'x + (9 - ((y * 2) / 3) + 1)'
# expr = 'x + (9 - ((y * 2) / 3) + 1)'
expr = 'x + (9 - ((y * 2) / (3) + 1)'


tem_erro = False

# Percorrer a expressão em busca de parenteses
for pos in range(len(expr)):
    if expr[pos] == '(':
        analisador.push(pos)
    elif expr[pos] == ')':
        # Se a pilha estiver vazia, temos um erro
        if analisador.is_empty:
            print(f"Erro: fecha parenteses na posição {pos} não tem o abre correspondente")
            tem_erro = True
        else:
            # Tira a posição abre da pilha
            pos_abre = analisador.pop()
            print(f"Abre parenteses da posição {pos_abre} correspondente ao fecha parenteses da posição")

while not analisador.is_empty:
    pos_abre = analisador.pop()
# Verifica se há sobras na pilha 
if not tem_erro:
    print('*** PARENTESES CORRETAMENTE BALANCEADOS ***')
else:
    while not analisador.is_empty:
        pos_abre = analisador.pop()
        print(f"Erro: abre parenteses na posição {pos_abre} não tem o fecha parenteses correspondente")