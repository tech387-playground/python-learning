### 13. Write a program that accepts a word from the user and reverse it.
### • Sample word: 'DZONI'
### • Expected Result : 'INOZD'

rijec = str(input("Unesi rijec: "))
duzina = len(rijec)
rijec_unazad = str('')
for x in range(duzina-1,-1,-1):
    rijec_unazad+=rijec[x]

print(rijec_unazad)