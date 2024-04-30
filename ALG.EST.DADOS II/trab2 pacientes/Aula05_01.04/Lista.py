class Paciente:
    def __init__(self, nome, idade, registro_medico):
        self.nome = nome
        self.idade = idade
        self.registro_medico = int(registro_medico)
        self.proximo = None

class ListaPaciente:
    def __init__(self):
        self.primeiro = None

    def tamanho(self):
        qt = 0
        paciente = self.primeiro
        while paciente is not None:
            paciente = paciente.proximo
            qt += 1
        return qt

    def add_paciente(self, nome, idade, registro_medico):
        novo_paciente = Paciente(nome, idade, registro_medico)

        if self.primeiro is None or self.primeiro.registro_medico >= novo_paciente.registro_medico:
            novo_paciente.proximo = self.primeiro
            self.primeiro = novo_paciente
        else:
            atual = self.primeiro
            while atual.proximo and atual.proximo.registro_medico < novo_paciente.registro_medico:
                atual = atual.proximo
            novo_paciente.proximo = atual.proximo
            atual.proximo = novo_paciente



        # if self.primeiro is None:
        #     self.primeiro = novo_paciente
        # else:
        #     paciente_atual = self.primeiro
        #     while paciente_atual.proximo is not None:
        #         paciente_atual = paciente_atual.proximo
        #     paciente_atual.proximo = novo_paciente

    def busca_paciente(self, registro_medico):
        paciente_atual = self.primeiro

        while paciente_atual is not None:
            if paciente_atual.registro_medico == registro_medico:
                return paciente_atual
            paciente_atual = paciente_atual.proximo

        return None

    def lista_pacientes(self):
        if self.primeiro is None:
            print("A lista de pacientes está vazia.")
        else:
            paciente_atual = self.primeiro
            while paciente_atual is not None:
                print(f"Nome: {paciente_atual.nome}, Idade: {paciente_atual.idade}, Prontuário: {paciente_atual.registro_medico}")
                paciente_atual = paciente_atual.proximo



    def counting_pacientes(self):
        maior_prontuario = 0
        atual = self.primeiro
        while atual:
            # print(atual.registro_medico, type(atual.registro_medico))
            # print(maior_prontuario, type(maior_prontuario))
            if int(atual.registro_medico) > maior_prontuario:
                maior_prontuario = atual.registro_medico
            atual = atual.proximo

        # Array de contagem
        count = [None] * (maior_prontuario + 1)

        # Preenchendo o array de contagem com referências aos pacientes
        atual = self.primeiro
        while atual:
            if count [atual.registro_medico] is None:
                count[atual.registro_medico] = []
            count[atual.registro_medico].append(atual)
            atual = atual.proximo

        # Reconstruindo a lista com base no array de contagem
        self.primeiro = None
        for prontuarios in reversed(count):
            if prontuarios is not None:
                for paciente in prontuarios:
                    paciente.proximo = self.primeiro
                    self.primeiro = paciente


    

















        # lista_pacientes = self.lista_pacientes
        # size = len(lista_pacientes)
        # output = [0] * size
        # count = [0] * 10

        # for i in range(0, size):
        #     count[lista_pacientes[i]] += 1

        # for i in range(1, 10):
        #     count[i] += count[i - 1]

        # i = size - 1
        # while i >= 0:
        #     output[count[lista_pacientes[i]] - 1] = lista_pacientes[i]
        #     count[lista_pacientes[i]] -= 1
        #     i -= 1

        # for i in range(0, size):
        #     lista_pacientes[i] = output[i]

        # return lista_pacientes
