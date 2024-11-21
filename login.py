import tkinter as tk

#Janela CRIAR CONTA
def Janela_CriarConta():

    janela2 = tk.Toplevel()
    janela2.title('Criar Conta')

    janela2.resizable(False,False)

    janela.rowconfigure(0,weight=1)
    janela.columnconfigure(0,weight=1)

    Cor_01 = tk.Label(janela2,text='Criar Conta',fg='Black', bg='#C0C0C0',width=40,height=3,font=10)
    Cor_01.grid(row=0,column=0,sticky='NSEW',columnspan=5)

    Cor_02 = tk.Label(janela2,fg='Black', bg='#C0C0C0',width=40,height=1)
    Cor_02.grid(row=14,column=0,sticky='NSEW',columnspan=5)

    #Espaços em Branco
    CorB_01 = tk.Label(janela2)
    CorB_01.grid(row=1,column=1)

    CorB_02 = tk.Label(janela2)
    CorB_02.grid(row=3,column=1)

    CorB_03 = tk.Label(janela2)
    CorB_03.grid(row=5,column=1)

    CorB_04 = tk.Label(janela2)
    CorB_04.grid(row=7,column=1)
    
    CorB_05 = tk.Label(janela2)
    CorB_05.grid(row=4,column=1)

    CorB_06 = tk.Label(janela2)
    CorB_06.grid(row=12,column=1)

    #Entrada Usuário
    TextoNome = tk.Label(janela2,text='Nome:')
    TextoNome.grid(row=2,column=1)

    Usuario = tk.Text(janela2,width=35,height=1)
    Usuario.grid(row=2,column=2)
    
    TextoEmail = tk.Label(janela2,text='Email:')
    TextoEmail.grid(row=4,column=1)

    Email = tk.Text(janela2,width=35,height=1)
    Email.grid(row=4,column=2)

    #Entrada Senha
    TextoSenha = tk.Label(janela2,text='Senha:')
    TextoSenha.grid(row=6,column=1)

    Senha1 = tk.Text(janela2,width=35,height=1)
    Senha1.grid(row=6,column=2)

    #Confirmar Senha
    ConfirmarSenha = tk.Label(janela2,text='Confirmar Senha:')
    ConfirmarSenha.grid(row=11,column=1)

    Senha2 = tk.Text(janela2,width=35,height=1)
    Senha2.grid(row=11,column=2)

    #Botão
    ConfirmarConta = tk.Button(janela2,text='Confirmar',command=janela2.destroy)
    ConfirmarConta.grid(row=13,columnspan=4)


#Janela LOGIN
janela = tk.Tk()
janela.title('Login')

janela.resizable(False,False)

janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

#Cores Fundo
Cor_01 = tk.Label(text='LOGIN',fg='Black', bg='#C0C0C0',width=40,height=3,font=10)
Cor_01.grid(row=0,column=1,sticky='NSEW',columnspan=4)

Cor_02 = tk.Label(fg='Black', bg='#C0C0C0',width=40,height=1)
Cor_02.grid(row=10,column=1,sticky='NSEW',columnspan=4)

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
TextoUsuario = tk.Label(text='Usuário:(Email)')
TextoUsuario.grid(row=2,column=1)

Usuario = tk.Text(width=35,height=1)
Usuario.grid(row=2,column=2)

#Entrada Senha
TextoSenha = tk.Label(text='Senha:')
TextoSenha.grid(row=4,column=1)

Senha = tk.Text(width=35,height=1)
Senha.grid(row=4,column=2)

#Botão
BotaoLogin = tk.Button(text='Confirmar Login')
BotaoLogin.grid(row=6,columnspan=4)

botao = tk.Button(janela, text='Criar Conta', command= Janela_CriarConta)
botao.grid(row=9,columnspan=4)

janela.mainloop()
