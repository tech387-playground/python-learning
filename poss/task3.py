
listaArtikala = ["Majica23", "Majica24"]
while True:
    artikal = input("Unesi artikal: ")
    if artikal not in listaArtikala:
        userNumber = listaArtikala.append(artikal)
        print(listaArtikala)
    else:
        print(f'{artikal} artikal vec postoji {listaArtikala}')


