import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename = 'cosmo')
window.title('Seting some Widgets')
window.geometry('500x500')

label = ttk.Label(
    master=window,
    text= 'Widgets'
    )
label.pack(pady=10)

Entry = ttk.Entry(
    master=window,
)
Entry.pack(pady=10)


btnPress = 0
def btnFunc():
    #global puxa variavel globalmente
    global btnPress
    btnPress += 1
    # ['attr'] configura atributo específico
    label['text'] = f"Button was pressed {btnPress} times"

    #.Configure() configura atributos de um Widget
    output.configure(text = Entry.get(), state='enabled')

Button = ttk.Button(
    master=window,
    text='Function',
    command=btnFunc
)

Button.pack()

output = ttk.Label(
    master=window,
    text= '',
    state='disabled'
    )
output.pack(pady=10)

window.mainloop()
