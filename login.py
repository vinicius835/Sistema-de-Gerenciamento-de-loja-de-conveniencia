# Prototipo - 03
import tkinter as tk
from tkinter import messagebox
import mysql.connector

#   Banco de Dados
conexao = mysql.connector.connect(
    host='localhost', 
    user='root',        
    password='',        
    database='lojanome'
)

#   Criação e Validação Cliente
def CriarConta_Info():
    nome_2 = Usuario2.get()
    email_2 = Email.get()
    senha01_2 = Senha1.get()
    senha02_2 = Senha2.get()

    if not nome_2 or not email_2 or not senha01_2 or not senha02_2:
        messagebox.showerror("ERRO","Todos os campos devem ser preenchidos!")
        return
    if senha01_2 != senha02_2:
        messagebox.showerror("ERRO","As senhas não coincidem")
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuario (Nome, Email, Senha) VALUES (%s, %s, %s)"
        valores = (nome_2, email_2, senha01_2)
        cursor.execute(sql, valores)
        conexao.commit()
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        cursor.close() 
    finally:
        if 'cursor' in locals():
            cursor.close()

#   Validar Login
def Validar_Login():
    email_1 = Usuario1.get()
    senha_1 = Senha3.get()

    try:
        # Buscar dados e validar -> (email e senha)
        cursor = conexao.cursor()
        sql = "SELECT * FROM usuario WHERE Email = %s AND Senha = %s"
        valores = (email_1, senha_1)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "USUÁRIO ou SENHA não encontrado ou incorretos!")
    finally:
        if 'cursor' in locals():
            cursor.close()

#   Janela 02 - Criar Conta 
def CriarConta_Janela():
    global janela2
    janela2 = tk.Toplevel()
    janela2. title("Criar Conta")
    janela2.resizable(False, False)

    TextoConta = tk.Label(janela2, text="Criar Conta", font=("Arial", 16), bg="#C0C0C0", height=2)
    TextoConta.grid(row=0,columnspan=2,sticky="NSEW")

#   Entrada Usuário
    global Usuario2
    Usuario2 = tk.Entry(janela2,width=30)
    Usuario2.grid(row=1,column=1,sticky="E")
    TextoUser2 = tk.Label(janela2, text="Nome:")
    TextoUser2.grid(row=1,column=0,sticky="E")

#   Entrada Email
    global Email
    Email = tk.Entry(janela2,width=30)
    Email.grid(row=2, column=1)
    TextoEmail = tk.Label(janela2,text="Email:")
    TextoEmail.grid(row=2,column=0,sticky="E")

#   Entrada Senhas
#   Senha 01
    global Senha1
    Senha1 = tk.Entry(janela2,width=30)
    Senha1.grid(row=3,column=1)
    TextoSe1 = tk.Label(janela2, text="Senha:")
    TextoSe1.grid(row=3, column=0, sticky="E")
#   Senha 02 Confirmação
    global Senha2
    Senha2 = tk.Entry(janela2, show="*", width=30)
    Senha2.grid(row=4, column=1, sticky="E")
    TextoSe2 = tk.Label(janela2, text="Confirmar Senha:")
    TextoSe2.grid(row=4, column=0)
    
#   Botão 02 - Confirmar Criação Conta
    Botao2 = tk.Button(janela2, text="Confirmar", command=CriarConta_Info)
    Botao2.grid(row=5, columnspan=2, pady=10)

#   Janela 01 - Login
janela = tk.Tk()
janela.title("Login")
janela.resizable(False, False)

#   Texto Login
TextoLogin = tk.Label(janela,text="LOGIN", font=("Arial", 16), bg="#C0C0C0", height=2)
TextoLogin.grid(row=0, columnspan=2, sticky="NSEW")

#   Entrada Usuario (Email)
global Usuario1
Usuario1 = tk.Entry(janela,width=30)
Usuario1.grid(row=1, column=1)
TextoUser1 = tk.Label(janela, text="Usuário (Email:)")
TextoUser1.grid(row=1, column=0, sticky="E")

#   Entrada Senha
global Senha3
Senha3 =tk.Entry(janela, show="*", width=30,)
Senha3.grid(row=2, column=1)
TextoSe3 = tk.Label(janela,text="Senha:")
TextoSe3.grid(row=2, column=0, sticky="E")

#   Botão 03 - Janela Criar Conta
Botao3 = tk.Button(janela,text="Criar Conta", command=CriarConta_Janela)
Botao3.grid(row=4,columnspan=2)

#   Cor - Janela
Cor = tk.Label(janela,bg="#C0C0C0", height=1)
Cor.grid(row=5,columnspan=2,sticky="NSEW")

#   Botão 01 - Confirmar Login
Botao1 = tk.Button(janela, text="Confirmar Login",command=Validar_Login)
Botao1.grid(row=3, columnspan=2, pady=10)

janela.mainloop()
