### 15. Write a program to check the validity of password input by users.  
###   Validation :
### • At least 1 letter between [a-z] and 1 letter between [A-Z].
### • At least 1 number between [0-9].
### • At least 1 character from [$#@].
### • Minimum length 6 characters.
### • Maximum length 16 characters.

lozinka = str(input("Enter password: "))
mala_slova = int(0)
velika_slova = int(0)
brojevi = int(0)
special_characters = int(0)
razmak = int(0)
for x in range (0, len(lozinka)):
    if(ord(lozinka[x])>=65 and ord(lozinka[x])<=90):
        velika_slova+=1
    if(ord(lozinka[x])>=97 and ord(lozinka[x])<=122):
        mala_slova+=1
    if(ord(lozinka[x])>=48 and ord(lozinka[x])<=57):
        brojevi+=1
    if((ord(lozinka[x])>=33 and ord(lozinka[x])<=47) or (ord(lozinka[x])>=58 and ord(lozinka[x])<=64) or (ord(lozinka[x])>=91 and ord(lozinka[x])<=96) or (ord(lozinka[x])>=123 and ord(lozinka[x])<=126)):
        special_characters+=1
    if(ord(lozinka[x])==32):
        razmak+=1

if(mala_slova==0):
    print('Lozinka ne sadrzi mala slova')
if(velika_slova==0):
    print('Lozinka ne sadrzi velika slova')
if(brojevi==0):
    print('Lozinka ne sadrzi brojeve')
if(special_characters==0):
    print('Lozinka ne sadrzi specijalne karaktere')
if(razmak>0):
    print('Nije dozvoljeno koristiti razmak')
if(len(lozinka)<6 or len(lozinka)>16):
    print('Lozinka ne smije sadrzavati manje od 6, a vise od 16 karaktera')
if(mala_slova>0 and velika_slova>0 and brojevi>0 and special_characters>0 and razmak==0 and (len(lozinka)>=6 and len(lozinka)<=16)):
    print('Lozinka je validna!!!')
else:
    print('Lozinka nije validna!!!')