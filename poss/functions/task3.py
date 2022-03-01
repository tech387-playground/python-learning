
import re


def provjera(unesi):
 izbaciSpace = re.sub(r" ", "", unesi)
 if izbaciSpace == izbaciSpace[::-1]:
      print("true")
 else:
      print("false")



provjera("koba")
provjera("ana")
provjera("Ana voli milovana")
