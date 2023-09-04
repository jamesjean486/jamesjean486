from Aluno import Classmate
class SeniorClassmate(Classmate):
    def __init__(self, cod, nome, matricula, semestre):
        super().__init__(cod, nome, matricula)
        self.semester = semestre


    def printing(self):
        print("CODE: " , self.id)
        print("NAME: " , self.name)
        print("MATRICULA: " , self.register)
        print("SEMESTER: " , self.semester)
        