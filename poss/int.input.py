listaBrojeva = [1,2,3]
while True:
    broj = int(input("unesi broj : "))
    if broj not in listaBrojeva:
        brojKojiJeUserUnio = listaBrojeva.append(broj)
        print (listaBrojeva)
    else:
        print(f'{broj} vec postoji na listi')