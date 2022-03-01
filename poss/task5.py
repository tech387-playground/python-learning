import datetime
from tkinter import Y


x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d"), x.strftime("%H-%M-%S"))
print(x)