# Write a program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(int(50)):
    if x == 0:
        print("nula nije djeljiva")
    if x % 3 == 0:
        print(str(x) + " Fizz")
    if x % 5 ==0:
        print(str(x) + " Buzz")
    if x % 3 ==0 and x % 5 == 0:
        print(str(x) + " FizzBuzz")