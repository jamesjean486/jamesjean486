# método q Ñ recebe parametro e possui retorno

def getPI():
    return 3.14

def getDobro_PI():
    return getPI() * 2



# método q Ñ recebe parametro e Ñ possui retorno


def pritingPI():
    print (getPI() )

# método q recebe parametro e possui retorno 

def getAreaCirculo(raio):
    return getPI() * (raio*raio)    


# método q recebe parametro e  Ñ possui retorno 

def printingAreaCirculo(raio):
    print(getAreaCirculo(raio))



#execução

pritingPI()
print(getAreaCirculo(6*2))
