import random
import time

class SortingAlgorithms:
    @staticmethod
    def select(arr):
        n = len(arr)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    @staticmethod
    def inserir(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    @staticmethod
    def bb(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    @staticmethod
    def ms(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            SortingAlgorithms.ms(L)
            SortingAlgorithms.ms(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def qs(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.qs(left) + middle + SortingAlgorithms.qs(right)

listaA = [820, 239, 771, 781, 977, 603, 883, 996, 466, 469, 324, 757, 921, 588, 618, 678, 629, 452, 341, 496, 565, 151, 107, 426, 838]
listaB = [45, 2, 50, 167, 0, 49, 7, 7, 18, 38, 90, 9, 1, 15, 85, 1, 0, 3, 87, 245, 9, 21, 67, 134, 25]
listaC = list("abacaxi")
listaD = ['Jose', 'Fabiano', 'Cristina', 'Ana Vitoria', 'Fabricio', 'Ricardo', 'Josefa', 'Esmeralda', 'Priscila', 'Zenaide', 'Antonio', 'Cristovao', 'Pedro', 'Maria', 'Nivaldo']

listas = [listaA, listaB, listaC, listaD]
algoritmos = [SortingAlgorithms.select, SortingAlgorithms.inserir, SortingAlgorithms.bb, SortingAlgorithms.ms, SortingAlgorithms.qs]

for lista in listas:
    for algoritmo in algoritmos:
        arr_copy = lista.copy()
        start_time = time.time()
        algoritmo(arr_copy)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Tempo de execução de {algoritmo.__name__} para a lista {lista}: {execution_time:.4f} ms")

numerosAleatorios = random.sample(range(1, 1000), 500)
for algoritmo in algoritmos:
    arr_copy = numerosAleatorios.copy()
    start_time = time.time()
    algoritmo(arr_copy)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print(f"Tempo de execução de {algoritmo.__name__} para a lista aleatória: {execution_time:.4f} ms")


#2: 
    # sim, utilizar um método de ordenação pode ajudar no processo de busca linear em uma lista numérica com 10.000 elementos, mas apenas em alguns casos específicos. 

    #Quando a ordenação é vantajosa:
#Listas estáticas: Se a lista não for modificada com frequência, o custo de ordenação pode ser amortizado ao longo de várias pesquisas.
#Valores de busca próximos: Se você sabe que o valor que está procurando está próximo do início ou do final da lista ordenada, a pesquisa linear pode ser mais eficiente do que em uma lista não ordenada.
    
''' Código questão 2
def busca_linear_nao_ordenada(lista, valor):
  for elemento in lista:
    if elemento == valor:
      return True
  return False

def busca_linear_ordenada(lista, valor):
  lista.sort()
  for elemento in lista:
    if elemento == valor:
      return True
  return False

lista_nao_ordenada = [5, 2, 4, 6, 1, 3]
lista_ordenada = lista_nao_ordenada[:]
lista_ordenada.sort()

valor_a_procurar = 3

encontrado_nao_ordenada = busca_linear_nao_ordenada(lista_nao_ordenada, valor_a_procurar)
encontrado_ordenada = busca_linear_ordenada(lista_ordenada, valor_a_procurar)

print(f"Encontrado em lista não ordenada: {encontrado_nao_ordenada}")
print(f"Encontrado em lista ordenada: {encontrado_ordenada}")
'''