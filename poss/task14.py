pitanje = str(input("sta zelite unijeti F or C: ")) 
if pitanje == str("F"): 
    farad = int(input("unesi farad:"))
    if farad != "":
      resultInCelsius = int((farad-32) * 5/9)
      print("to ti je " + str(resultInCelsius) + "°C")
    else:
      print("nije")
if pitanje == str("C"): 
     celzijus = (int(input("unesi celzijus:")))
     if int(celzijus) != "" or celzijus.isdigit():
      resultInFarad = int((celzijus * 9/5) + 32)
      print("to ti je " + str(resultInFarad) + "°F") 
elif pitanje != str("F") or pitanje != str("F"): 
    print("Mozes unijeti samo C ili F") 

    print(pitanje[:1:-1])
