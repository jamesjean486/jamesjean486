from Pessoa import Person
class Physical(Person):
    def __init__(self, nome, telefone, cpf):
        super().__init__(self, nome, telefone)
        self.cpf = cpf
        print("Physical person Created!")

    def __str__(self):
        return super().__str__()

    def __str__():
        pass