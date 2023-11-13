precos = [ 4.00, 8.00, 20.00 ]

def aumentarPreco( x ):
    return x*1.1


novosPrecos = map(aumentarPreco, precos )
print(list(novosPrecos)) 
print("\n", "############################################", "\n")
valores = [(10,20) , [30,40]]

def somar(x):
    return x[0] + x[1]

somas = map(somar ,valores)
print(list(somas))