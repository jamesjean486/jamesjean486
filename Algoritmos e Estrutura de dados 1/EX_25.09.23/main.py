from Notebook import Note
from Desktop import Desktop

machine1 = Note("Positivo", "Prateado", 755.49, "48h")
machine2 = Desktop("IntelCore7", "Black", 3758.00,"500W")

print(machine1.getInformacoes())
print(machine2.getInformacoes())
