import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title('Login')

janela.resizable(False,False)

janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

#Cores Fundo
# Row 00
Cor_01 = tk.Label(text='LOGIN',fg='Black', bg='#C0C0C0',width=40,height=3,font=10)
Cor_01.grid(row=0,column=1,sticky='NSEW',columnspan=4)
# Row 06
Cor_02 = tk.Label(fg='Black', bg='#C0C0C0',width=40,height=1)
Cor_02.grid(row=8,column=1,sticky='NSEW',columnspan=4)

#Espaço em Branco
# Row 01
CorB_01 = tk.Label()
CorB_01.grid(row=1,column=1)
# Row 02
CorB_02 = tk.Label()
CorB_02.grid(row=3,column=1)

# Row 05
CorB_02 = tk.Label()
CorB_02.grid(row=5,column=1)

# Row 07
CorB_03 = tk.Label()
CorB_03.grid(row=7,column=1)

#Entrada Usuário
TextoUsuario = tk.Label(text='Usuário:')
TextoUsuario.grid(row=2,column=1)

Usuario = tk.Text(width=35,height=1)
Usuario.grid(row=2,column=2)

#Entrada Senha
TextoSenha = tk.Label(text='Senha:')
TextoSenha.grid(row=4,column=1)

Senha = tk.Text(width=35,height=1)
Senha.grid(row=4,column=2)

#Botão Confirmação
BotaoLogin = tk.Button(text='Confirmar Login')
BotaoLogin.grid(row=6,columnspan=3)

# Informações Login (Usuário e Senha)
def InfoLogin():
    print()

janela.mainloop()