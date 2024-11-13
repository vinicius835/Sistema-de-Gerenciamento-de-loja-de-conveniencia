import tkinter as tk

janela = tk.Tk()
janela.title('Login')

janela.resizable(False,False)

janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

#Cores Fundo
Cor_01 = tk.Label(text='LOGIN',fg='Black', bg='#C0C0C0',width=40,height=3,font=10)
Cor_01.grid(row=0,column=1,sticky='NSEW',columnspan=4)

Cor_02 = tk.Label(fg='Black', bg='#C0C0C0',width=40,height=1)
Cor_02.grid(row=9,column=1,sticky='NSEW',columnspan=4)

#Espaços em Branco
CorB_01 = tk.Label()
CorB_01.grid(row=1,column=1)

CorB_02 = tk.Label()
CorB_02.grid(row=3,column=1)

CorB_03 = tk.Label()
CorB_03.grid(row=5,column=1)

CorB_04 = tk.Label()
CorB_04.grid(row=7,column=1)

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
BotaoLogin.grid(row=6,columnspan=4)


# Informações Login (Usuário e Senha)
janela.mainloop()
