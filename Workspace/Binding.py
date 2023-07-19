import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename='minty')
window.title('Combo Box')
window.geometry("300x300")

items = ('Item-1',
        'Item-2',
        'Item-3',
        'Item-4',
        'Item-5',
        'Item-6',
        'Item-7',
        'Item-8',
        'Item-9',
        'Item-10',
        )

# Select box the options are on the tuple named as items that are set on the ['value']
Select_box = ttk.Combobox(
    master=window,
    textvariable='Select an Item'
)
Select_box['value'] = items

Select_box.pack(pady=100)
window.mainloop()
