import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='litera')
window.title('Binding')
window.geometry("300x300")

title_label = ttk.Label(
    master=window,
    text='Enter Your Name',
    font='Arial 18 bold',
    )

output_label = ttk.Label(
    master=window,
    text='',
    )


String_Var = tk.StringVar()
Entry = ttk.Entry(
    master=window,
    textvariable=String_Var
)

def function():
    print(String_Var.get())
    output_label['text'] = String_Var.get()

Button = ttk.Button(
    master=window,
    text='Press',
    command=function
    )

title_label.pack(pady=5,padx=10)
Entry.pack(pady=10,padx=10)
Button.pack(pady=10,padx=10)
output_label.pack()
#Para Quando apertar Enter/Return Executar a função
window.bind('<Return>', lambda event: function())
window.mainloop()
