class Queue:

    """ Método construtor """
    def __init__(self):
        self.__data = []   # Inicializa uma lista vazia

    def enqueue(self, val):
    # Insere val no final (topo) da pilha
        self.__data.append(val)

    """ Método para remoção
        Nome padronizado: 
    """

    def dequeue(self):
        if self.is_empty:
            raise Exception('ERRO: Impossível remover de uma fila vazia')
        
            # Remove o primeiro elemento da fila 
        return self.__data.pop(0)

    """
        Método que consulta o valor no topo da pilha, sem retirá-lo de lá
        Nome padronizado: peek()
    """
    def peek(self):
        if self.is_empty:
            raise Exception('ERRO: impossível consultar a cabeça de uma fila vazia')
        # Retorna o último elemento da lista
        return self.__data[0]

    
    """
        Método que permite imprimir a fila
        Esse é um método especial do Python: __str__
    """
    def __str__(self):
        return str(self.__data)
   
    
    """
        Propriedade somente-leitura que informa se a pilha está 
        vazia (True) ou não (False)
    """
    @property
    def is_empty(self):
        return len(self.__data) == 0