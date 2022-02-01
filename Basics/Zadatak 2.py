### 2. Write a program that prints True or False whether a number is within 1000 or 2000(both upper and lower limit included).
### Sample value: 1303
### Expected Result : True


num = int(input('Enter the number: '))

if num>=1000 and num<=2000:
    print('True')
else:
    print('False')