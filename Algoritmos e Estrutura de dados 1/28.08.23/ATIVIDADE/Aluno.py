class Classmate:
    def __init__(self, codigo, nome, matricula):
        self.id = codigo
        self.name = nome 
        self.register = matricula

    def printing(self):
        print("CODE: " + self.id)
        print("NAME: " + self.name)
        print("ACADEMIC REGISTRATION: " + self.register)
        