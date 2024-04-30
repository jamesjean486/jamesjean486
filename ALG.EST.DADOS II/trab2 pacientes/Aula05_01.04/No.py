class Paciente:
    def __init__(self, nome, idade, registro_medico):
        self.nome = nome
        self.idade = idade
        self.registro_medico = registro_medico
        self.proximo = None