### 14. Write a program to convert temperatures to and from celsius, fahrenheit.  
###   [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
### • Expected Output :  
###   60°C is 140 in Fahrenheit  
###   45°F is 7 in Celsius

temp = input('Unesi temperaturu: ')
if((ord(temp[-1])==99 or ord(temp[-1])==67) and len(temp)>1):
    vrijednost_temperature_u_c = int(temp[0:-1])
    vrijednost_temperature_u_f = int(vrijednost_temperature_u_c*9/5 + 32)
    print(vrijednost_temperature_u_c, '°C is', vrijednost_temperature_u_f, 'in Fahrenheit')
elif((ord(temp[-1])==102 or ord(temp[-1])==70) and len(temp)>1):
    vrijednost_temperature_u_f = int(temp[0:-1])
    vrijednost_temperature_u_c = int((5/9)*(vrijednost_temperature_u_f-32))
    print(vrijednost_temperature_u_f, '°F is', vrijednost_temperature_u_c, 'in Celsius')
else:
    print('Pogresan unos!!!')