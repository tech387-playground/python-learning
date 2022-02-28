# 4. Write a function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"



from contextlib import redirect_stderr
import string
alphabet = string.ascii_lowercase
list_alpha = list(string.ascii_lowercase)
def is_it_pangram(recenica):
    for x in list_alpha:
        if not x in recenica:
            return 'String nije pangram'
    
    return 'String je pangram'


#Primjer kad string nije pangram
var1 = 'ABCDkdedokfnAKLNOI'
var1 = var1.lower()
print(is_it_pangram(var1))

# Primjer kad je string pangram
var1 = 'The quick brown fox jumps over the lazy dog'
var1 = var1.lower()
print(is_it_pangram(var1))
