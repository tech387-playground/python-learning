### 3. Write a program that accepts an integer (n) and computes the value of n+nn+nnn.
### • Sample value of n is 5
### • Expected Result : 615

n = int(input('Enter a number: '))
nn = n*11
nnn= n*111
suma = n+nn+nnn
print("Zbir brojeva ", n, ", ", nn, "i ", nnn, "iznosi ", suma)