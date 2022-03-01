#Write a function that takes one argument. If the function receives value equal to "yes", it should return "Shutting down". Alternatively, if value is equal to "no", then the function should return "Shutdown aborted". Finally, if gets anything other than those inputs, the function should return "Sorry".
def Prva(argument):
    if argument == "yes":
        return "Shutting down"
    if argument == "no":
        return "Shutdown aborted"
    else:
        return "sorry"
        
unesi = input("unesi yes or no:")
print(Prva(unesi))
