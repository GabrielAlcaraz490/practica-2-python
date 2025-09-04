print("dame tu frase")

palabra = ""

frase = input()
listita = frase.split()

print(listita)
for continua in listita:
    print(continua.upper())

print("dame una palabra")
palabra = input()
veces = listita.count(palabra)  

print(f"palabra {palabra} sale {veces} veces")

print("por favor dame la palabra que deseas reemplazar")

