import random


def gerador_de_lista_com_elementos_inteiros(tamanho_lista:int = 10, intervalo_maximo:int = 10) -> list:
    """Recebe como parâmetro o 'tamanho_lista', gerando elementos entre '0' e
        o intervalo_maximo informado.
       Caso não informado o tamanho a lista, retorna com tamanho padrão 10 elementos.
       Caso não informado o intervalo máximo gerado, o padrão é 10.
    """
#    lista = [random.randint(0, intervalo_maximo) for _ in range(tamanho_lista)]
    lista_de_inteiros = random.sample(range(0, intervalo_maximo), tamanho_lista)

    print(f"\nVocê gerou uma lista de elementos inteiros e aleatórios.")
    print(f"A lista gerada possui {len(lista_de_inteiros)} elementos.")
    print(f"Os elementos gerados estão entre 0 e {intervalo_maximo}.")
    input("Enter.")
    return lista_de_inteiros
