import mod_cnpj as cnpj
from tkinter import *


def run_result():
    text_cnpj = cnpj.generator()
    result_text.delete(1.0, END)
    result_text.insert(INSERT, text_cnpj)



window = Tk()
window.geometry('220x300')
window.resizable(width=False, height=False)
window.title('CNPJ GENERATOR')

bg = PhotoImage(file='bg.png')
background = Label(window, image=bg)
background.place(x=0,y=0)

orientation_text = Label(window, text='CNPJ Generator', font='Unispace 8 bold', bg='white')
orientation_text.grid(column=0, row=2, padx=25, pady=54)

button = Button(window, text='Click to generate a CNPJ', command=run_result,font='Unispace 8', bg='black', fg='orange', justify=CENTER)
button.grid(column=0, row=3, padx=25, pady=10)

result_text = Text(window, width=17, height=1, font='ComicSans 10 bold')
result_text.grid(column=0, row=5, padx=25, pady=10)

window.mainloop()
