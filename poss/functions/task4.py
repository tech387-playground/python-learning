from ast import While
import re

input = input("unesi:")
# flag = 0
# while True:
# 	if not re.search("[a]" and "[b]" and "[c]" and "[d]", input):
# 		flag = -1
# 		break
# 	else:
# 		flag = 0
# 		print("imaju sva slova u mom slucaju ne abece nego abcd")
# 		break

# if flag == -1:
# 	print("u recenici nemaju sva slova abecede")

def provjeriRecenicu(nestoNegdje):
	if re.search("[a]" and "[b]" and "[c]" and "[d]", input):
		return "sva slova ABCD su tu"
	else:
		return 

		 

#  while True:
# 	 if not re.search("[a]" and "[b]" and "[c]" and "[d]", input):
#           return ""
#           break
#  if not re.search("[a-z]", input):
#      return "stanje"


	

print(provjeriRecenicu(input))
   







# uneseno = input("unesi recenicu")
# provjera(uneseno)
# print(provjera)


