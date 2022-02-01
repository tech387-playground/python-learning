### 10. Write a program that creates sentences from the words in a list.
### • Sample list: ['In', 'the', 'last', 'episode', 'of', 'Breaking', 'Bad']
### • Expected Result : 'In the last episode of Breaking Bad'

list1 = ['Ovo', 'je', 'lista', 'rijeci', 'koju', 'treba', 'pretvoriti', 'u', 'recenicu']
recenica = str('')
for x in list1:
    recenica = recenica + x + ' '

print(recenica)