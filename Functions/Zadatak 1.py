# 1. Write a function that takes one argument. If the function receives value equal to "yes",
# it should return "Shutting down". Alternatively, if value is equal to "no",
# then the function should return "Shutdown aborted". Finally, if gets anything other than those inputs,
# the function should return "Sorry".


def turn_off(x):
    if(x=='yes'):
        return('Shutting down')
    elif(x=='no'):
        return('Shutdown aborted')
    else:
        return('Sorry')

# Deklaranija varijable koja ce biti koristena kao argument funkije
var1 = input('Do you want turn off your computer?')
# Deklaranija varijable koja ce biti jednaka responsu funkcije
# (funkcija ce vratiti neku vrijednost koja ce biti spremljena u ovu varijablu)
response_from_function = turn_off(var1)
# Ispis variajable koja je dobila vrijednost vracenu iz funkcije
print(response_from_function)