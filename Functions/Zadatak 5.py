# 5. Write a function that invokes a lambda/anonymous function after specific milliseconds.


from cProfile import label
import threading

def fun():
    print('Funckija je pozvana')



waiting_time = int(input('Unesi delay time: '))
print('Vrijeme cekanja u milisekundama iznosi: ')
print((lambda a : a*1000)(waiting_time))


#timer = threading.Timer(waiting_time, fun)
#timer.start()