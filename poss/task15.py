# 15. Write a program to check the validity of password input by users.  
#    Validation :
# • At least 1 letter between [a-z] and 1 letter between [A-Z].
# • At least 1 number between [0-9].
# • At least 1 character from [$#@].
# • Minimum length 6 characters.
# • Maximum length 16 characters.


import re
password = input("enter pass")
flag = 0
while True:
	if (len(password)<6 and len(password)>16):
		flag = -1
		break
	elif not re.search("[a-z]", password):
		flag = -1
		break
	elif not re.search("[A-Z]", password):
		flag = -1
		break
	elif not re.search("[0-9]", password):
		flag = -1
		break
	elif not re.search("[$#@]", password):
		flag = -1
		break
	else:
		flag = 0
		print("Loading homepage")
		break

if flag == -1:
	print("Password nije dobar, mora biti jedno malo, jednoveliko, manje od 16 a vise od 6")
