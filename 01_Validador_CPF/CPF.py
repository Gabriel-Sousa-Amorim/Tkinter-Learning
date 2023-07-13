import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
#Criação da Janela

window = ttk.Window(themename = 'journal')
#Mudança do Título
window.title('Validação de CPF')
#Tamanho da Janela
window.geometry('300x300')

def Convert():
    CPF = Entry_Label_Var.get()
    print(CPF)
    soma = 0
    if (len(str(CPF)) >= 12):
        Output_Label_str.set('Inválido, CPF maior que o nescessário')
    elif (len(str(CPF)) <= 10):
        Output_Label_str.set('Inválido, CPF menor que o nescessário')
    else:
        if (CPF == 11111111111 or
            CPF == 22222222222 or
            CPF == 33333333333 or
            CPF == 44444444444 or
            CPF == 55555555555 or
            CPF == 66666666666 or
            CPF == 77777777777 or
            CPF == 88888888888 or
            CPF == 99999999999 or
            CPF == 00000000000) :
            Output_Label_str.set('CPF Inválido')
        else:
            list_CPF = [int(i) for i in str(CPF)]
            i = 0
            j = 10
            vf = 0
            for i in range(9):
                acumulator = list_CPF[i] * j
                j = j -1
                soma = soma + acumulator
            vf = (soma * 10)%11
            if (str(vf) == str(list_CPF[9])):
                i = 0
                j = 11
                soma = 0
                for i in range(10):
                    acumulator = list_CPF[i] * j
                    j = j -1
                    soma = soma + acumulator
                vf = (soma * 10)%11
                if (str(vf) == str(list_CPF[10])):
                    Output_Label_str.set('CPF Válido')
                else:
                    Output_Label_str.set('CPF Inválido')
            else:
                Output_Label_str.set('CPF Inválido')
#Título dentro do programa
Title_Label = ttk.Label(
    #Onde o frame se localizará
    master = window,
    #Conteúdo da Label
    text = 'Validador CPF.',
    #Fonte da Label
    font= 'Calibri 24 bold',
    #Cor da Labe
    )
#Campo de Escrita

Input_Label = ttk.Label(
    master=window,
    )

Entry_Label_Var = tk.IntVar()
Entry_Label = ttk.Entry(
    master=Input_Label,
    textvariable = Entry_Label_Var
    )

Btn_Label = ttk.Button(
    master=Input_Label,
    text='Convert',
    command=Convert,
    padding='10px'
    )

#Título dentro do programa
Output_Label_str = tk.StringVar()
Output_Label_str.set('Resultado')
Output_Label = ttk.Label(
    #Onde o frame se localizará
    master = window,
    #Conteúdo da Label
    text = 'Result is:',
    textvariable= Output_Label_str,
    )
#Campo de Escrita

Title_Label.pack()
Input_Label.pack()
Entry_Label.pack(pady= 10)
Btn_Label.pack(pady= 10)
Output_Label.pack(pady= 10)


window.mainloop()
