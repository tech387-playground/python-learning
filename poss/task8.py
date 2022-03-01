from multiprocessing.sharedctypes import Value


list = [2, 2, 5, 1]
y = 0
for x in list:
    y=x+y
sum = list[0] + list[1] + list[2] + list[3]
print(sum)


