#import os

#os.system("phpstorm")
#os.system("google")

import tkinter

window = tkinter.Tk()

window.title('Bot control')
window.geometry('500x300')

lbl1 = tkinter.Label(window, text='name')
ent1 = tkinter.Entry(window)
lbl2 = tkinter.Label(window, text='password')
ent2 = tkinter.Entry(window)
btn = tkinter.Button(window, text='Button')

#buld grid
lbl1.pack()
ent1.pack()
lbl2.pack()
ent2.pack()
btn.pack()


window.mainloop() 

