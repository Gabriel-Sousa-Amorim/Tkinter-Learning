import tkinter as tk
import ttkbootstrap as ttk

#window
window = ttk.Window(themename='cyborg')
window.title('Variables')
window.geometry('300x300')

strVar = tk.StringVar(value= 'Press')


label = ttk.Label(
    master = window,
    text = 'Variable label',
    textvariable = strVar
    )

entry1 = ttk.Entry(
    master = window,
    textvariable = strVar
    )

def btnFunc():
    print(strVar.get())
btn = ttk.Button(
    master = window,
    command = btnFunc,
    textvariable = strVar
    )
label.pack(pady=10)
entry1.pack(pady=10)
btn.pack(pady=10)


strVar2 = tk.StringVar(value= 'teste')
label2 = ttk.Label(
    master = window,
    text = 'Variable label',
    textvariable = strVar2
    )
entry2 = ttk.Entry(
    master = window,
    textvariable = strVar2
    )
entry3 = ttk.Entry(
    master = window,
    textvariable = strVar2
    )
label2.pack(pady=10)
entry2.pack(pady=10)
entry3.pack(pady=10)

entry4 = tk.Checkbutton(master=window)
entry4.pack()
window.mainloop()
