### 7. Write a program to find word in a string.
### • Sample string: Today was a good day.
### • Sample word: good
### • Expected Result : True

recenica = str(input("Unesi recenicu: "))

rijec = str(input("Unesi rijec koji zelite pronaci: "))

x = recenica.find(rijec)

if x!=-1:
    print("True")
else:
    print("False")