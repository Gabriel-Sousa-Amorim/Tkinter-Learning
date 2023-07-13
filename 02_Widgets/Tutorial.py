import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename= 'darkly')
#Título Janela
window.title('Parte 2')
#Tamanho da Janela
window.geometry('400x500')


#Um texto presente na janela raiz
ttk.Label(
    master=window,
    text='Escreva o quanto você ama a Bia').pack(padx=5)


#Um campo para escrever textos presente na janela raiz
ttk.Text(master=window).pack(padx=10, pady=10)


def buttonFunc():
    print('button was pressed')

#Um botão para escrever textos presente na Entry
ttk.Button(
    master=window,
    command=buttonFunc,
    text='Press'
).pack(side='right')

def ExerciseFunc():
    print('Hello')

ttk.Button(
    master=window,
    command= lambda: print('Hello'),
    text='Press'
).pack(side='left')

window.mainloop()

