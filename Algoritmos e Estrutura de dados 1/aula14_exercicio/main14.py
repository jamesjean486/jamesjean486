from torre import Tower
from apartamento import Apartemento
from fila import Fila
from lista import Lista
t1 = Tower("Tower C", " Rua Riddler ,100")
t2 = Tower("Tower A", " Rua Joker ,200")

ap1 = Apartemento("101 - A", t1)
ap2 = Apartemento("707 - B", t2)
ap3 = Apartemento("401 - A", t2)
ap4 = Apartemento("202 - B", t1)
ap5 = Apartemento("512 - A", t1)
ap6 = Apartemento("102 - B", t2)
ap7 = Apartemento("404 - B", t2)
ap8 = Apartemento("777 - A", t1)

semVagas = Fila()
apsComVaga = Lista()

semVagas.add(ap1)
semVagas.add(ap2)
semVagas.add(ap3)
semVagas.add(ap4)
semVagas.add(ap5)
semVagas.add(ap6)
semVagas.add(ap7)
semVagas.add(ap8)

ap = semVagas.remover(1)
apsComVaga.add(ap)


