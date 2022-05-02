from lib.queue import Queue

fila = Queue()
fila.enqueue('Mariovaldo')
fila.enqueue('Belarmina')
fila.enqueue('Valdisney')

print(fila)

atendido = fila.dequeue()
print('Atendido: ', atendido)

proximo = fila.peek()
print('Próximo: ', proximo)

print(fila)

fila.enqueue('Gercina')
fila.enqueue('Ladislau')

print(fila)