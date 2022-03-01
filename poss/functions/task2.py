# Write a function that accepts 2 arguments, first one is any given data type, second one is user input value. Function should check if the input value satisfies the data type condition of the first argument.






def dvatipa(type, bilosta):
    if type == int and bilosta == int:
        return "isti tipovi"
    if type == str and bilosta == str:
        return "isti tipovi"
    else:
        return "nisu isti"

print(dvatipa(str, "kokalo"))

# #ovo je kad su isti
# unesiNesto = int(input("unesi broj ili string:"))
# print(dvatipa(int, unesiNesto))
