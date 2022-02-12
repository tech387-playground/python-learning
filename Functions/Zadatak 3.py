# 3. Write a function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# Examples:   'Ana voli Milovana',  'madam',  'U Rimu umiru',  'idu ljeta, pate ljudi'  itd.



from audioop import reverse


def is_it_polindrom(recenica):
    recenica_unazad = recenica[::-1]
    if(recenica==recenica_unazad):
        print('String je polindrom')
    if(recenica!=recenica_unazad):
        print('String nije polindrom')

var1 = str('Ana VOli MILOvana')
var1 = var1.lower()
var1 = var1.replace(' ','')

is_it_polindrom(var1)

is_it_polindrom('123456')

