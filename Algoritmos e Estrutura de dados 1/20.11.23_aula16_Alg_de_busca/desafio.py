v = [2, 3, 6, 8, 10, 14, 19, 22, 29, 37, 41, 45, 50, 53, 56, 65, 72, 77, 87, 91, 98]
def busca_sequencial(v, valor):
    iteracoes = 0
    for i in range(len(v)):
        iteracoes += 1
        if v[i] == valor:
            return True, iteracoes
    return False, iteracoes

def busca_binaria(v, valor):
    iteracoes = 0
    inicio = 0
    fim = len(v) - 1

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if v[meio] == valor:
            return True, iteracoes
        elif v[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return False, iteracoes

procurar_valor = int(input("Informe o valor que deseja procurar: "))

sequencial, it_sequencial = busca_sequencial(v, procurar_valor)
print(f"Busca Sequencial: Valor encontrado? {sequencial}. Iterações: {it_sequencial}")

binaria, it_binarias = busca_binaria(v, procurar_valor)
print(f"Busca Binária: Valor encontrado? {binaria}. Iterações: {it_binarias}")

