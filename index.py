import random
def gerador_de_lista_com_elementos_inteiros(tamanho_lista:int = 10, intervalo_maximo:int = 10) -> list:
    if intervalo_maximo < tamanho_lista:
        return None

    lista_de_inteiros = random.sample(range(0, intervalo_maximo))

    return lista_de_inteiros

def busca_sequencial(valor:int = 0, lista: list = []) -> int:
    if len(lista) == 0:
        return None

    try:
        x = lista.index(valor)
    except:
        return None

    return x 


lista =  gerador_de_lista_com_elementos_inteiros (10 , 40)
print(lista)
print(len(lista))

print(busca_sequencial(25, lista))
