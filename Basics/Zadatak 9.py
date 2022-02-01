### 9. Write a program to remove duplicates from a list.
### • Sample list: [2, 2, 5, 1]
### • Expected Result : [2, 5, 1]

list1 = [1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5]

for x in list1:
    while list1.count(x) > 1:
        list1.remove(x)

print(list1)
