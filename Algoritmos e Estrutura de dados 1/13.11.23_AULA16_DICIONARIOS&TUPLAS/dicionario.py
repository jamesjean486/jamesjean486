moto = {
    "marca" : "Yamaha",
    "ano" :2020 , 
    "Cilindradas" : 321 
}

print(moto)
print("marca, " , moto["marca"])
print(moto.keys())
print("------------------------------------")


for chave, valor in moto.items():
    print(chave,  " - ", valor)

print("____________________________________\n")


for chave in moto.keys():
    print(chave,  " - ", moto[chave])
print("\n","---------------------" "\n")
    
son1 = {"name":"Julia", "Age":15}
son2 = {"name":"Adam", "Age":12}
son3 = {"name":"Helena", "Age":3}

childrens = son1, son2
print(childrens)
son2["name"] = "Helena"
print(childrens)
del son1["name"]
son1["nickname"] = "Juh"
print(childrens)