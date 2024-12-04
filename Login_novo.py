# - - - Prototipo 04 - - - 
# -> Sem banco de dados (sql)
# -> Para teste
def login():
    import tkinter as tk
    from tkinter import messagebox
  
    usuarios = {}
    global usuario_logado
    usuario_logado = False

    # Criar Conta - Cliente
    def CriarConta_Info():
        nome_2 = Usuario2.get()
        email_2 = Email.get()
        senha01_2 = Senha1.get()
        senha02_2 = Senha2.get()

        if not nome_2 or not email_2 or not senha01_2 or not senha02_2:
            messagebox.showerror("ERRO", "Todos os campos devem ser preenchidos!")
            return
        if len(senha01_2) < 6:
            messagebox.showerror("ERRO", "A senha deve ter pelo menos 6 caracteres!")
            return
        if senha01_2 != senha02_2:
            messagebox.showerror("ERRO", "As senhas não coincidem!")
            return
          
        usuarios[email_2] = {"nome": nome_2, "senha": senha01_2}
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")

    # Validar Login
    def Validar_Login():
        nonlocal usuario_logado
        email_1 = Usuario1.get()
        senha_1 = Senha3.get()

        if email_1 in usuarios and usuarios[email_1]["senha"] == senha_1:
            usuario_logado = True
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            # Habilitar o botão  -> Confirmar comprar
            BotaoConfirmarCompra.config(state="normal")  # Habilitar o botão
        else:
            usuario_logado = False
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
          
    def ConfirmarCompra():
        if usuario_logado:
            messagebox.showinfo("Compra", "Compra confirmada com sucesso!")
        else:
            messagebox.showerror("Erro", "Você precisa estar logado para confirmar a compra!")

    # Janela 02 - Criar Conta
    def CriarConta_Janela():
        janela2 = tk.Toplevel()
        janela2.title("Criar Conta")
        janela2.resizable(False, False)

        TextoConta = tk.Label(janela2, text="Criar Conta", font=("Arial", 16), bg="#C0C0C0", height=2)
        TextoConta.grid(row=0, columnspan=2, sticky="NSEW")

        # Entrada Usuário
        global Usuario2
        Usuario2 = tk.Entry(janela2, width=30)
        Usuario2.grid(row=1, column=1, sticky="E")
        TextoUser2 = tk.Label(janela2, text="Nome:")
        TextoUser2.grid(row=1, column=0, sticky="E")

        # Entrada Email
        global Email
        Email = tk.Entry(janela2, width=30)
        Email.grid(row=2, column=1)
        TextoEmail = tk.Label(janela2, text="Email:")
        TextoEmail.grid(row=2, column=0, sticky="E")

        # Entrada Senhas
        global Senha1
        Senha1 = tk.Entry(janela2, width=30)
        Senha1.grid(row=3, column=1)
        TextoSe1 = tk.Label(janela2, text="Senha:")
        TextoSe1.grid(row=3, column=0, sticky="E")

        global Senha2
        Senha2 = tk.Entry(janela2, show="*", width=30)
        Senha2.grid(row=4, column=1, sticky="E")
        TextoSe2 = tk.Label(janela2, text="Confirmar Senha:")
        TextoSe2.grid(row=4, column=0)

        # Botão - Confirmar Criação Conta
        Botao2 = tk.Button(janela2, text="Confirmar", command=CriarConta_Info)
        Botao2.grid(row=5, columnspan=2, pady=10)

    # Janela 01 - Login
    janela = tk.Tk()
    janela.title("Login")
    janela.resizable(False, False)

    # Texto Login
    TextoLogin = tk.Label(janela, text="LOGIN", font=("Arial", 16), bg="#C0C0C0", height=2)
    TextoLogin.grid(row=0, columnspan=2, sticky="NSEW")

    # Entrada Usuário (Email)
    global Usuario1
    Usuario1 = tk.Entry(janela, width=30)
    Usuario1.grid(row=1, column=1)
    TextoUser1 = tk.Label(janela, text="Usuário (Email):")
    TextoUser1.grid(row=1, column=0, sticky="E")

    # Entrada Senha
    global Senha3
    Senha3 = tk.Entry(janela, show="*", width=30)
    Senha3.grid(row=2, column=1)
    TextoSe3 = tk.Label(janela, text="Senha:")
    TextoSe3.grid(row=2, column=0, sticky="E")

    # Botão - Criar Conta
    Botao3 = tk.Button(janela, text="Criar Conta", command=CriarConta_Janela)
    Botao3.grid(row=4, columnspan=2)

    # Cor - Janela
    Cor = tk.Label(janela, bg="#C0C0C0", height=1)
    Cor.grid(row=5, columnspan=2, sticky="NSEW")

    # Botão - Confirmar Login
    Botao1 = tk.Button(janela, text="Confirmar Login", command=Validar_Login)
    Botao1.grid(row=3, columnspan=2, pady=10)

    # Botão - Confirmar Compra
    global BotaoConfirmarCompra
    BotaoConfirmarCompra = tk.Button(janela, text="Confirmar Compra", command=ConfirmarCompra, state="disabled")
    BotaoConfirmarCompra.grid(row=6, columnspan=2, pady=10)

    janela.mainloop()
