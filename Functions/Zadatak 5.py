# 5. Write a function that invokes a lambda/anonymous function after specific milliseconds.


import threading
from time import sleep

def fun():
    print('Funckija je pozvana')



waiting_time = int(input('Unesi delay time: '))
#waiting_time = waiting_time/1000
#sleep(waiting_time)
#print('Vrijeme cekanja u satima iznosi: ')
#print((lambda a : a/60)(waiting_time))
y = lambda : print('20')
timer = threading.Timer(waiting_time, y())
timer.start()