from Aluno import Classmate
class HSClassmate(Classmate):
    def __init__(self, cod, nome, matricula, ano):
        super().__init__(cod, nome, matricula)
        self.year = ano


    def printing(self):
        print("CODE: " , self.id)
        print("NAME: " , self.name)
        print("MATRICULA: " , self.register)
        print("YEAR: " , self.year)
        