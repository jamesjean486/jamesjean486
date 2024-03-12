import random


def gerador_de_listas_inteiro(qtdelements,valormaximo):
    lista = []
    for x in range (qtdelements):
        lista.append(random.randint(1 , valormaximo))
    
    return lista

lista = gerador_de_listas_inteiro(10,50)




def gerador_de_listas_inteiro(tamanho_lista:int=10, intervalo_max:int=10):
    if intervalo_max < tamanho_lista:
        return None
    lista_de_inteiros = random.sample(range(0, intervalo_max))

    return lista_de_inteiros

lista_gerada = gerador_de_listas_inteiro(tamanho_lista= 10, intervalo_max= 50)
print(lista_gerada)