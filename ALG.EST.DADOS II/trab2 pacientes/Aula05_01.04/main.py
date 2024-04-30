from Lista import ListaPaciente

lista_de_pacientes = ListaPaciente()
lista_de_pacientes.add_paciente("Alice", 30, "5")
lista_de_pacientes.add_paciente("Bob", 24, "1")
lista_de_pacientes.add_paciente("Steve", 25, "7")
lista_de_pacientes.add_paciente("Maxuel", 22, "2")
lista_de_pacientes.add_paciente("Jessica", 31, "4")
lista_de_pacientes.add_paciente("Marcus", 12, "8")
lista_de_pacientes.add_paciente("Pamela", 28, "3")
lista_de_pacientes.add_paciente("Carrie", 50, "9")
lista_de_pacientes.add_paciente("Robert", 28, "6")
lista_de_pacientes.add_paciente("Tommy", 24, "10")

print("Antes do Counting Sort:")
lista_de_pacientes.lista_pacientes()

lista_de_pacientes.counting_pacientes()
print("\nDepois do Counting Sort:")
lista_de_pacientes.lista_pacientes()